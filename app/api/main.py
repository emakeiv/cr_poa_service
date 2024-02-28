import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI
from app.api.endpoints import documents, home, model

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository, ServisoKatalogasRepository


engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('poa_doc_sample_repo', PowerOfAttorneyDocumentSampleRepository)
repository_registry.add('serviso_katalogo_repo', ServisoKatalogasRepository)

def create_server(repositories=None):
    server = FastAPI(debug=True)
    server.include_router(home.router)
    server.include_router(documents.router)
    server.include_router(model.router)
    server.repositories = repositories
    return server


app = create_server(repositories=repository_registry)
