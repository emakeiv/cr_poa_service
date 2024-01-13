from fastapi import UploadFile, File
from pydantic import BaseModel

class DocumentRequestSchema(BaseModel):
    file: UploadFile = File(...)

class DocumentResponsetSchema(BaseModel):
    text: str