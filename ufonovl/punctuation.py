import spacy

def segment_sents(text, newlines):
    nlp = spacy.load("en_core_web_lg", exclude=["ner", "parser", "tagger", "lemmatizer"])
    nlp.enable_pipe("senter")
    doc = nlp(text)
    text_sents = [sent.text.replace('\n', newlines) if newlines else sent.text for sent in doc.sents]
    return text_sents