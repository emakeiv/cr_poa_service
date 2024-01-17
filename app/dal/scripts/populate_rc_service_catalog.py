import boto3
import pandas as pd
from io import BytesIO

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dal.models.service_catalog_model import ServisoKatalogas
from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import (
    ServisoKatalogasRepository
)
from app.utils.common import (
    convert_to_activity,
    convert_to_bool,
    convert_to_date,
    convert_to_int
)

s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='aws_admin',
    aws_secret_access_key='aws_admin'
)

bucket_name = 'rc-service-catalog'
file_key = 'service_catalog.xlsx'

try:
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_data = BytesIO(obj['Body'].read())
    df = pd.read_excel(file_data)
   

    engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
    session = sessionmaker(bind=engine)()

    repository_registry = RepositoryRegistry(session)
    repository_registry.add('serviso_katalogo_repo', ServisoKatalogasRepository)
    if not df.empty:
        records = []
        service_catalog_repo = repository_registry.get('serviso_katalogo_repo')
        for index, row in df.iterrows():
            try:
                record = ServisoKatalogas(
                    id=row['Nr.'],
                    paslaugos_kodas=row['Paslaugos kodas'],
                    institucijos_kodas=convert_to_int(row['Institucijos kodas']),
                    institucijos_pavadinimas=row['Institucijos pavadinimas'],
                    paslaugos_pavadinimas=row['Paslaugos pavadinimas (LT)'],
                    paslaugos_tipas=row['Paslaugos tipas'],
                    el_paslauga=row['E. paslauga'],
                    tik_notarinis=convert_to_bool(row['Tik notarinis']),
                    prokuratura=convert_to_bool(row['Prokūra']),
                    aktyvumas=convert_to_activity(row['Aktyvumas']),
                    galioja_nuo=pd.to_datetime(row['Galioja nuo']).date(),
                    galioja_iki=convert_to_date(row['Galioja iki']),
                )
                records.append(record.dict())
            except Exception as e:
                    print(f"An error occurred adding record to the list: {e}")
        
        if records:
            try:
                service_catalog_repo.bulk_insert(records)
            except Exception as e:
                print(f"An error occurred adding recrods to database: {e}")

except Exception as e:
    print(f"An error occurred populating_rc_service_catalog records: {e}")