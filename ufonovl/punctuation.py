import spacy
import re

def segment_sents(text, newlines=False):
    nlp = spacy.load("en_core_web_lg", exclude=["ner", "parser", "tagger", "lemmatizer"])
    nlp.enable_pipe("senter")
    doc = nlp(text)
    text_sents = []
    for sent in doc.sents:
        if newlines:
            sent_text = sent.text.replace('\n', newlines)
        else:
            sent_text = sent.text
        sent_text = re.sub("^ ", "", sent_text)
        text_sents.append(sent_text)
        
    return text_sents