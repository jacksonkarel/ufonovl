import argparse
from ufonovl.reddit.feed import new_reddit_posts
from ufonovl.reddit.history import reddit_history
from ufonovl.reddit.subreddits_total import subreddits_total
from ufonovl.reddit.jsonl_to_txt import jsonl_to_txt

def cli_parser():
    utn_parser = argparse.ArgumentParser(description='An NLP pipeline that detects new textual information about UFOs/UAPs')
    utn_parser.add_argument('interval', action='store', choices=['new', 'old', 'total', 'convert'], help="Process new reddit posts, old reddit posts, get the total number of reddit posts, or convert data from jsonl to txt.")

    args = utn_parser.parse_args()

    interval = args.interval

    # if interval == "new":
    #     new_reddit_posts(subreddit)

    if interval == "old":
        reddit_history()
    
    elif interval == "total":
        subreddits_total()
    
    elif interval == "convert":
        jsonl_to_txt()