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

def mine_reddit(reddit_query, sub_names):
    reddit = reddit_api()
    subreddit = reddit.subreddit(sub_names)
    spec_r_q = reddit_query(subreddit)
    r_add_punct(spec_r_q, r_api_subm_seg)

def r_subm_segment(sub_title, selftext):
    title_sents = segment_sents(sub_title)
    stext_sents = segment_sents(selftext, ' ')
    text_sents = title_sents + stext_sents
    return text_sents

def r_api_subm_seg(submission):
    text_sents = r_subm_segment(submission.title, submission.selftext)
    return text_sents

def r_json_subm_seg(submission):
    text_sents = r_subm_segment(submission["title"], submission["selftext"])
    return text_sents

def r_add_punct(posts, source_seg, dn=False):
    if dn:
        queries = []
    pcftc = punct_file_corpus()
    for r_post in posts:
        text_sents = source_seg(r_post)
        for sentence in text_sents:
            if sentence not in pcftc:
                
                if dn:
                    queries.append(sentence)

                nl_query = "\n" + sentence
                with open("data/punct.txt", 'a') as f:
                    f.write(nl_query) 
    
    detect_novelty(pcftc, queries)
    