from apscheduler.schedulers.background import BlockingScheduler

from mine_reddit import mine_reddit, reddit_hour

mine_reddit_hour = mine_reddit(reddit_hour)

scheduler = BlockingScheduler()
job = scheduler.add_job(mine_reddit_hour, 'interval', hours=1)
scheduler.start()