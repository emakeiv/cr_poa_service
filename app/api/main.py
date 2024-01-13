from fastapi import FastAPI
from api.endpoints import documents, home

def create_server():
    server = FastAPI(debug=True)
    server.include_router(home.router)
    server.include_router(documents.router)
    return server


app = create_server()