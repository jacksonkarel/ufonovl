from sentence_transformers import SentenceTransformer, util
import torch

def detect_novelty(corpus, queries):

    # Modified from https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/semantic-search/semantic_search.py
    
    # This is a simple application for sentence embeddings: semantic search

    # We have a corpus with various sentences. Then, for a given query sentence,
    # we want to find the most similar sentence in this corpus.

    # This script outputs for various queries the top 5 most similar sentences in the corpus.

    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

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
            
            for score, idx in zip(top_results[0], top_results[1]):
                rating_log = "\n{} (Score: {:.4f})".format(query, score)
        
        with open("logs/log.txt", 'a') as f:
            f.write(rating_log)