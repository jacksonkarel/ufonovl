import re

import spacy
from spacy.lang.en import English
from tqdm import tqdm

def segment_sents(*args, newlines=False):
    nlp.enable_pipe("senter")
    nlp = spacy.load("en_core_web_lg", exclude=["ner", "parser", "tagger", "lemmatizer"])
    text_sents = []
    for txt in args: 
        doc = nlp(txt)
        for sent in doc.sents:
            if newlines:
                sent_text = sent.text.replace('\n', newlines)
            else:
                sent_text = sent.text
            sent_text = re.sub("^ ", "", sent_text)
            text_sents.append(sent_text)
        
    return text_sents

def segment_sents_fast(texts):
    nlp = English()
    nlp.add_pipe("sentencizer")
    text_sents = []
    for doc in tqdm(nlp.pipe(texts)):
        for sent in doc.sents:
            sent_text = sent.text
            sent_text = re.sub("^ ", "", sent_text)
            text_sents.append(sent_text)
    return text_sents
            
        