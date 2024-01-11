from fastapi import APIRouter

from src.enter import search_wiki

router = APIRouter()

@router.get("/search/{value}", tags=["search"])
async def root(value: str):
    result = search_wiki(value)
    return {"result": result}