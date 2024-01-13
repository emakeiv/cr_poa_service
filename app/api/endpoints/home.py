from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to the Registry Center Power of Attorney authorization service"}