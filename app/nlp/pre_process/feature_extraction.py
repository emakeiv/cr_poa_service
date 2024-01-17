from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.dal.repo.registry import RepositoryRegistry
from app.dal.repo.impl import PowerOfAttorneyDocumentSampleRepository

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

engine = create_engine('postgresql://admin:admin@localhost/rc_poa_main_db')
session = sessionmaker(bind=engine)()

repository_registry = RepositoryRegistry(session)
repository_registry.add('poa_doc_sample_repo', PowerOfAttorneyDocumentSampleRepository)
poa_doc_sample_repo = repository_registry.get('poa_doc_sample_repo')

documents = [record['processed_document_content'] for record in poa_doc_sample_repo.list()]
labels = np.ones(len(documents))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)


# X_train, X_temp, y_train, y_temp = train_test_split(X, labels, test_size=0.4, random_state=42)
# X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)


