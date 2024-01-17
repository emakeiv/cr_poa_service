from app.dal.models.base_model import Base

from sqlalchemy import (
   Column, 
   Integer, 
   String, 
   LargeBinary, 
   Date
)

class PowerOfAttorneyDocumentSample(Base):
    
    __tablename__ = 'igaliojimo_dokumentu_pavyzdziai'
    __metadata__ = Base.metadata
    
    id = Column(Integer, primary_key=True)
    document_name = Column(String)
    document_content = Column(String)
    processed_document_content = Column(String) 
    processed_date = Column(Date)
    

    def dict(self):
        return {
            "id": self.id,
            "document_name": self.document_name,
            "document_content": self.document_content,
            "processed_document_content": self.processed_document_content,
            "processed_date": self.processed_date
        }