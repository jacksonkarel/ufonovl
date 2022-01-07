from apscheduler.schedulers.background import BlockingScheduler

from get_reddit import get_reddit

get_reddit()

scheduler = BlockingScheduler()
job = scheduler.add_job(get_reddit, 'interval', hours=1)
scheduler.start()