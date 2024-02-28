import string
import spacy
nlp_lt = spacy.load("lt_core_news_md")

def normalize_text(text):
    text = text.lower().replace('\n', ' ')
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def remove_stopwords_and_lemmatize(text):
    doc = nlp_lt(text)
    tokens = [token.lemma_ for token in doc if token.text.strip() != ""]
    return " ".join(tokens)

def debug_preprocessing(text, nlp_pipeline=nlp_lt):
    print("Original text:", text)

    normalized_text = normalize_text(text)
    print("Normalized text:", normalized_text)

    doc = nlp_pipeline(normalized_text)
    for token in doc:
        print(f"Token: {token.text}, Lemma: {token.lemma_}, Stop word: {token.is_stop}")

    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
    print("Processed text:", processed_text)

    return processed_text
    

