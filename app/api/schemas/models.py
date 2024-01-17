from fastapi import UploadFile, File
from pydantic import BaseModel
from datetime import datetime

class DocumentRequestSchema(BaseModel):
    file: UploadFile = File(...)

class DocumentResponsetSchema(BaseModel):
    id: int
    document_name: str
    processed_document_content: str
    processed_date: datetime