import os

import praw
from sentence_transformers import SentenceTransformer, util
import torch

from punctuation import segment_sents


def file_to_corpus(filename):
    with open(filename) as f:
        punct_text = f.read()
    corpus = punct_text.split("\n")
    return corpus

def get_reddit():
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
    for submission in subreddit.top("hour"):
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

    """
    This is a simple application for sentence embeddings: semantic search

    We have a corpus with various sentences. Then, for a given query sentence,
    we want to find the most similar sentence in this corpus.

    This script outputs for various queries the top 5 most similar sentences in the corpus.
    """

    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    # Query sentences:
    # queries = ['A man is eating pasta.', 'Someone in a gorilla costume is playing a set of drums.', 'A cheetah chases prey on across a field.']
    # queries = ['A man is eating pasta.']

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    top_k = min(1, len(corpus))
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        if len(corpus) < 1000000:
            # Alternatively, we can also use util.semantic_search to perform cosine similarty + topk
            hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1)
            hit = hits[0][0]
            rating_log = "\n{} (Score: {:.4f})".format(query, hit['score'])
        
        else:
            # We use cosine-similarity and torch.topk to find the highest 5 scores
            cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
            top_results = torch.topk(cos_scores, k=top_k)

            # print(top_results[0], top_results[1])
            
            for score, idx in zip(top_results[0], top_results[1]):
                rating_log = "\n{} (Score: {:.4f})".format(query, score)
        
        with open("logs/log.txt", 'a') as f:
            f.write(rating_log)

        if query not in corpus:
            nl_query = "\n" + query
            with open("data/punct.txt", 'a') as f:
                f.write(nl_query)
    