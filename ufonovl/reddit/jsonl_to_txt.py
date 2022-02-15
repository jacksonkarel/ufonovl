import jsonlines

from ufonovl.reddit.mine import r_add_punct

def jsonl_to_txt():
    with jsonlines.open('data/ufos_reddit_submissions.jsonl') as reader:
        submissions = list(reader)
    subm_fields = ["title", "selftext"]
    r_add_punct(submissions, subm_fields)