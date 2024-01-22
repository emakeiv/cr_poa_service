import boto3
from io import BytesIO
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.dal.models.other_document_model import OtherDocumentSample
from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import OtherDocumentSampleRepository
from src.ocr.service import OpticalCharacterRecognitionService
# Initialize the S3 client
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='aws_admin',
    aws_secret_access_key='aws_admin'
)

bucket_name = 'other-doc-samples'

ocr_service = OpticalCharacterRecognitionService()

engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('other_doc_sample_repo', OtherDocumentSampleRepository)
other_doc_sample_repo = repository_registry.get('other_doc_sample_repo')

try:
    objects = s3_client.list_objects(Bucket=bucket_name)['Contents']
    records = []
    for obj in objects:
        file_name = obj['Key']
        file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        file_data = BytesIO(file_obj['Body'].read())

        ocr_text = ocr_service.process_image(file_data.getvalue())
        if ocr_text is not None:
            record = OtherDocumentSample(
                document_name=file_name, 
                document_content=ocr_text,
                processed_date=datetime.now().date(),
                )
            # entry = record.dict()
            # print(f"adding formatted record: {entry}")
            # records.append(entry)
            print(f"adding to db  record: {record.document_name}")
            other_doc_sample_repo.add(record)
    # if records:
    #     try:
    #         poa_doc_sample_repo.bulk_insert(records)
    #     except Exception as e:
    #         print(f"An error occurred adding recrods to database: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
