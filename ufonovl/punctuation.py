import re

import spacy
from spacy.lang.en import English
from tqdm import tqdm

def segment_sents(texts, newlines=False, fast=False):
    if fast:
        nlp = English()
        nlp.add_pipe("sentencizer")
    else:
        nlp = spacy.load("en_core_web_lg", exclude=["ner", "parser", "tagger", "lemmatizer"])
        nlp.enable_pipe("senter")
    text_sents = []
    texts_len = len(texts)
    with tqdm(total=texts_len) as pbar:
        for doc in nlp.pipe(texts):
            for sent in doc.sents:
                if newlines:
                    sent_text = sent.text.replace('\n', newlines)
                else:
                    sent_text = sent.text
                sent_text = re.sub("^ *", "", sent_text)
                text_sents.append(sent_text)
            pbar.update(1)
    
    return text_sents
            
        