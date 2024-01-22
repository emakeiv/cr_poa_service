from sqlalchemy import func

from app.dal.models.power_of_attorney_model import PowerOfAttorneyDocumentSample
from app.dal.models.other_document_model import OtherDocumentSample
from app.dal.models.service_catalog_model import ServisoKatalogas

from app.dal.repo.entity import RepositoryEntity

class PowerOfAttorneyDocumentSampleRepository(RepositoryEntity[PowerOfAttorneyDocumentSample]):
    def __init__(self, session):
        super().__init__(PowerOfAttorneyDocumentSample, session)

class OtherDocumentSampleRepository(RepositoryEntity[OtherDocumentSample]):
    def __init__(self, session):
        super().__init__(OtherDocumentSample, session)
        
class ServisoKatalogasRepository(RepositoryEntity[ServisoKatalogas]):
    def __init__(self, session):
        super().__init__(ServisoKatalogas, session)