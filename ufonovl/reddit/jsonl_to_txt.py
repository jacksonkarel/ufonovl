import jsonlines

from ufonovl.reddit.mine import r_add_punct, r_json_subm_seg

def jsonl_to_txt():
    with jsonlines.open('data/ufos_reddit_submissions.jsonl') as reader:
        r_add_punct(reader, r_json_subm_seg)

            