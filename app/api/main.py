import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI
from app.api.endpoints import documents, home

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository


engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('poa_doc_sample_repo', PowerOfAttorneyDocumentSampleRepository)


def create_server(repositories=None):
    server = FastAPI(debug=True)
    server.include_router(home.router)
    server.include_router(documents.router)
    server.repositories = repositories
    return server


app = create_server(repositories=repository_registry)