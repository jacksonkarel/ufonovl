import datetime as dt

from psaw import PushshiftAPI

from ufonovl.reddit.mine import reddit_subs_dn

def reddit_history():
    # UFOs subreddit created Mon Mar 10 2008 PDT (1205211399)
    # aliens subreddit created 1217838855
    # HighStrangeness subreddit created 1238686810
    start_epoch = 1205211399
    epochs = [start_epoch]
    for ep in epochs:
        p_shift_api = PushshiftAPI()

        submissions = list(p_shift_api.search_submissions(after=ep,
                                    sort='asc',
                                    subreddit='UFOs',
                                    filter=['title', 'selftext', 'id'],
                                    limit=100))
        reddit_subs_dn(submissions)
        last_sub_created = submissions[-1].created_utc
        with open("logs/time.txt", 'w') as f:
            f.write(last_sub_created)
        epochs.append(last_sub_created)
