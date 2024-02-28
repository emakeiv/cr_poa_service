
import spacy
import numpy as np
nlp_lt = spacy.load("lt_core_news_md")

def get_document_vector(text):
    """
    returns a vector representation of text by averaging word vectors.
    """
    doc = nlp_lt(text)
    vectors = [word.vector for word in doc if word.has_vector]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        # If no words with vectors, return zero vector
        return np.zeros((nlp_lt.vocab.vectors_length,))
