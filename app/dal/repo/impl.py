from sqlalchemy import func

from app.dal.models.power_of_attorney_model import PowerOfAttorneyDocumentSample
from app.dal.models.service_catalog_model import ServisoKatalogas

from app.dal.repo.entity import RepositoryEntity

class PowerOfAttorneyDocumentSampleRepository(RepositoryEntity[PowerOfAttorneyDocumentSample]):
    def __init__(self, session):
        super().__init__(PowerOfAttorneyDocumentSample, session)

class ServisoKatalogasRepository(RepositoryEntity[ServisoKatalogas]):
    def __init__(self, session):
        super().__init__(ServisoKatalogas, session)