import os

import praw

from ufonovl.punctuation import segment_sents
from ufonovl.detect_novelty import detect_novelty
from ufonovl.corpus import punct_file_corpus

def reddit_api():
    client_id = os.environ.get("REDDIT_ID")
    client_secret = os.environ.get("REDDIT_SEC")
    user_agent = os.environ.get("REDDIT_U_AGENT")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )
    return reddit

def mine_reddit(reddit_query):
    reddit = reddit_api()
    sub_names = "UFOs+aliens+HighStrangeness+ufo"
    subreddit = reddit.subreddit(sub_names)
    spec_r_q = reddit_query(subreddit)
    reddit_subs_dn(spec_r_q)

def reddit_subs_dn(submissions):
    queries = []
    for submission in submissions:
        texts = [submission.title, submission.selftext]
        for text in texts:
            if text == submission.title:
                newlines = False
            else:
                newlines = ' '
            text_sents = segment_sents(text, newlines)
            for sentence in text_sents:
                pcftc = punct_file_corpus()
                if sentence not in pcftc:
                    queries.append(sentence)
                    nl_query = "\n" + sentence
                    with open("data/punct.txt", 'a') as f:
                        f.write(nl_query)
    
    detect_novelty(pcftc, queries)
    