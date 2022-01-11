import os

import praw

from punctuation import segment_sents
from detect_novelty import detect_novelty


def file_to_corpus(filename):
    with open(filename) as f:
        punct_text = f.read()
    corpus = punct_text.split("\n")
    return corpus

def reddit_hour(subreddit):
    return subreddit.top("hour")

def mine_reddit(reddit_query):
    client_id = os.environ.get("REDDIT_ID")
    client_secret = os.environ.get("REDDIT_SEC")
    user_agent = os.environ.get("REDDIT_U_AGENT")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )
    sub_names = "UFOs+aliens+HighStrangeness+ufo"
    subreddit = reddit.subreddit(sub_names)
    corpus = file_to_corpus("data/punct.txt")
    queries = []
    spec_r_q = reddit_query(subreddit)
    for submission in spec_r_q:
        texts = [submission.title, submission.selftext]
        for text in texts:
            if text == submission.title:
                newlines = False
            else:
                newlines = ' '
            text_sents = segment_sents(text, newlines)
            for sentence in text_sents:
                if sentence not in corpus:
                    queries.append(sentence)
    
    detect_novelty(corpus, queries)
    