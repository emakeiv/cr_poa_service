from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException
)
from fastapi import UploadFile, File

from app.api import dependencies
from app.api.schemas.models import (
    DocumentRequestSchema, 
    DocumentResponsetSchema
)

router = APIRouter()

@router.post("/documents", tags=[""], response_model=DocumentResponsetSchema)
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