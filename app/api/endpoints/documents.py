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

from app.nlp.pre_process.data_prep import (
      normalize_text, 
      remove_stopwords_and_lemmatize
      )

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository

router = APIRouter()

@router.post("/ocr-service")
async def process_document(
    file: UploadFile = File(...),
    ocr_service = Depends(dependencies.get_ocr_service)
):
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=415, detail="Unsupported file type.")

    try:
        content = await file.read()
        text = ocr_service.process_image(content)
        #norm_text = normalize_text(text)
        #final_text = remove_stopwords_and_lemmatize(norm_text)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get-poa-services")
async def get_documents(request: Request):

        try:
            poa_doc_sample_repo = request.app.repositories.get('serviso_katalogo_repo')
            documents = poa_doc_sample_repo.list(limit=5) 
            return documents
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))