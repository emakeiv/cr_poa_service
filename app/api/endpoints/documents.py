from typing import List
from fastapi import (
    APIRouter, 
    Depends, 
    Request,
    HTTPException
)
from fastapi import UploadFile, File

from app.api import dependencies
from app.api.schemas.models import (
    DocumentRequestSchema, 
    DocumentResponsetSchema
)

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository

router = APIRouter()

@router.post("/send-documents", tags=[""], response_model=DocumentResponsetSchema)
async def process_document(
    file: UploadFile = File(...),
    ocr_service = Depends(dependencies.get_ocr_service)
):
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=415, detail="Unsupported file type.")

    try:
        content = await file.read()
        text = ocr_service.process_image(content)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get-documents")
async def get_documents(request: Request):

        try:
            poa_doc_sample_repo = request.app.repositories.get('poa_doc_sample_repo')
            documents = poa_doc_sample_repo.list(limit=5) 
            return documents
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))