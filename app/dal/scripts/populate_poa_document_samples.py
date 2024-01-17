import boto3
from io import BytesIO
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dal.models.power_of_attorney_model import PowerOfAttorneyDocumentSample
from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository
from src.ocr.service import OpticalCharacterRecognitionService
# Initialize the S3 client
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='aws_admin',
    aws_secret_access_key='aws_admin'
)

bucket_name = 'power-of-attorney-doc-samples'

ocr_service = OpticalCharacterRecognitionService()

engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('poa_doc_sample_repo', PowerOfAttorneyDocumentSampleRepository)
poa_doc_sample_repo = repository_registry.get('poa_doc_sample_repo')

try:
    objects = s3_client.list_objects(Bucket=bucket_name)['Contents']
    for obj in objects:
        file_name = obj['Key']
        file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_data = BytesIO(file_obj['Body'].read())


        ocr_text = ocr_service.process_image(file_data.getvalue())
        record = PowerOfAttorneyDocumentSample(
            document_name=file_name, 
            document_content=ocr_text,
            processed_date=datetime.now().date(),
            )
        poa_doc_sample_repo.add(record)
    session.commit()

except Exception as e:
    print(f"An error occurred: {e}")
