import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords_from_jd(jd_text):
    doc = nlp(jd_text)
    keywords = set()
    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip().lower()
        if len(phrase) > 2:
            keywords.add(phrase)
    return list(keywords)