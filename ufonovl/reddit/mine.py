import os
import re

import praw
from tqdm import tqdm

from ufonovl.punctuation import segment_sents, segment_sents_fast
from ufonovl.detect_novelty import detect_novelty
from ufonovl.corpus import punct_file_corpus
from ufonovl.helpers import list_diff

r_stop_phrases = ["[deleted]", "[removed]", "", " ", "."]

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
    r_add_punct(spec_r_q, r_api_texts, dn=True)

def r_subm_segment(sub_title, selftext):
    texts = [sub_title, selftext]
    stop_phrases = ["[deleted]", "[removed]"]
    texts_to_seg = list_diff(texts, stop_phrases)
    text_sents = segment_sents(*texts_to_seg)
    return text_sents

def r_api_texts(submission):
    new_sents = [submission.title, submission.selftext]
    return new_sents

def r_json_texts(submission):
    new_sents = [submission["title"]]
    if "selftext" in submission:
        new_sents.append(submission["selftext"])
    return new_sents

def check_stop_phra(txt, new_texts):
    if txt not in r_stop_phrases:
        new_texts.append(txt)
    return new_texts

def r_add_punct(posts, post_fields, post_attrs=False):
    if post_attrs:
        first_cl_posts = []
        for post in tqdm(posts):
            post_fields = post_attrs(post)
            for post_field in post_fields:
                first_cl_posts = check_stop_phra(post_field, first_cl_posts)
    else:
        ext_posts = []
        for post in tqdm(posts):
            for post_field in post_fields:
                if post_field in post:
                    ext_posts = check_stop_phra(post[post_field], ext_posts)
        nfsc_sents = []
        pcftc = punct_file_corpus()
        for sent in tqdm(pcftc):
            if re.search(".|!|?", sent) is False:
                nfsc_sents.append(sent)
        first_cl_posts = list_diff(ext_posts, nfsc_sents)

    if post_attrs:
        text_sents = segment_sents(*first_cl_posts)
        pcftc = punct_file_corpus()
    else:
        text_sents = segment_sents_fast(first_cl_posts)

    new_ts = list_diff(text_sents, pcftc)
    for sentence in tqdm(new_ts):
        nl_sent = "\n" + sentence
        with open("data/punct.txt", 'a') as f:
            f.write(nl_sent) 
    
    if post_attrs:
        pcftc += new_ts
        detect_novelty(pcftc, new_ts)
    