import datetime as dt

from psaw import PushshiftAPI
import praw

from ufonovl.reddit.mine import reddit_subs_dn

def reddit_history():
    api = PushshiftAPI()

    start_epoch=int(dt.datetime(2017, 1, 1).timestamp())

    submissions = list(api.search_submissions(after=start_epoch,
                                subreddit='UFOs',
                                filter=['title', 'selftext', 'id'],
                                limit=10))
    reddit_subs_dn(submissions)

# UFOs subreddit created Mon Mar 10 2008 PDT