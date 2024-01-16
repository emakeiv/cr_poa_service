import boto3
import pandas as pd
from io import BytesIO

# Boto3 client configuration for MinIO
s3_client = boto3.client('s3',
                         endpoint_url='http://minio-endpoint:9000',
                         aws_access_key_id='YOUR-ACCESSKEYID',
                         aws_secret_access_key='YOUR-SECRETACCESSKEY')

bucket_name = 'rc-service-catalog'
file_key = 'service_catalog.xlsx'

try:
    # Fetch the Excel file from MinIO
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_data = BytesIO(obj['Body'].read())

    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(file_data)

    # Create SQLAlchemy engine
    DATABASE_URL = "postgresql://user:password@localhost/dbname"
    engine = create_engine(DATABASE_URL)

    # Populate the database
    df.to_sql('service_catalog', engine, if_exists='replace', index=False)

except Exception as e:
    print("An error occurred:", e)
