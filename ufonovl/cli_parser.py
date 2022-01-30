import argparse
from ufonovl.reddit.feed import new_reddit_posts
from ufonovl.reddit.history import reddit_history

def cli_parser():
    utn_parser = argparse.ArgumentParser(description='An NLP pipeline that detects new textual information about UFOs/UAPs')

    utn_parser.add_argument('subreddit', help='Subreddit to be mined')
    utn_parser.add_argument('interval', action='store', choices=['new', 'old'], help="Process new or old reddit posts")
    utn_parser.add_argument('--start', help='Time to start processing old posts')

    args = utn_parser.parse_args()

    interval = args.interval
    subreddit = args.subreddit
    start_time = args.start

    if interval == "new":
        new_reddit_posts(subreddit)

    elif interval == "old":
        reddit_history(subreddit, start_time)