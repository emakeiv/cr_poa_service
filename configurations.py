from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    environment: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    pgdata: str
    pgadmin_default_email: str
    pgadmin_default_password: str
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_s3_bucket: str
    mlflow_db: str
    mlflow_storage: str
    
    class Config:
      env_file = ".env"
      env_file_encoding = 'utf-8'

main_settings = Settings()



