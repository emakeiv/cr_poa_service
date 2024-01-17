from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository
from app.dal.models.power_of_attorney_model import PowerOfAttorneyDocumentSample

from app.nlp.pre_process.data_prep import (
      normalize_text, 
      remove_stopwords_and_lemmatize,
      debug_preprocessing
      )

engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('poa_doc_sample_repo', PowerOfAttorneyDocumentSampleRepository)
poa_doc_sample_repo = repository_registry.get('poa_doc_sample_repo')

# Query the original documents
documents = poa_doc_sample_repo.list()

for document in documents:
    if len(document['document_content']) > 0:
        try:
            print(f"Processing document: {document['document_name']}, document characters length: {len(document['document_content'])}")
            norm_text = normalize_text(document['document_content'])
            final_text = remove_stopwords_and_lemmatize(norm_text)
            poa_doc_sample_repo.update(document['id'], processed_document_content=final_text)
        except Exception as e:
            print(f"Error processing document {document['document_name']}: {e}")
            
           
         
