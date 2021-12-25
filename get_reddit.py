import os

import praw

client_id = os.environ.get("REDDIT_ID")
client_secret = os.environ.get("REDDIT_SEC")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="macintosh:com.example.ufocompanies:v1.0.0 (by u/boo_hooray)",
)

subreddit = reddit.subreddit("UFOs")
for submission in subreddit.top("hour"):
    print(submission.title)