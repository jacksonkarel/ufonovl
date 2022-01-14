from apscheduler.schedulers.background import BlockingScheduler

from ufonovl.reddit.mine import mine_reddit

def reddit_hour(subreddit):
    return subreddit.top("hour")

def new_reddit_posts():
    mine_reddit_hour = mine_reddit(reddit_hour)

    scheduler = BlockingScheduler()
    job = scheduler.add_job(mine_reddit_hour, 'interval', hours=1)
    scheduler.start()