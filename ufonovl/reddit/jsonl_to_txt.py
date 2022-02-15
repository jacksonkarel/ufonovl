

import jsonlines

from ufonovl.reddit.mine import r_add_punct

def jl_paths_txt(jl_path, post_fields):
    with jsonlines.open(jl_path) as reader:
        posts = list(reader)
    r_add_punct(posts, post_fields)

def jsonl_to_txt():
    subm_jsonl_path = "data/ufos_reddit_submissions.jsonl"
    subm_fields = ["title", "selftext"]
    jl_paths_txt(subm_jsonl_path, subm_fields)
    comment_jl_path = "data/ufos_reddit_comments.jsonl"
    comment_fields = ["body"]
    jl_paths_txt(comment_jl_path, comment_fields)