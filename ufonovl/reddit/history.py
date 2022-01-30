from psaw import PushshiftAPI

from ufonovl.reddit.mine import reddit_subs_dn

def reddit_history(subreddit, start_time):
    # UFOs subreddit created Mon Mar 10 2008 PDT (1205211399)
    # aliens subreddit created 1217838855
    # HighStrangeness subreddit created 1238686810
    epochs = [start_time]
    for ep in epochs:
        p_shift_api = PushshiftAPI()

        submissions = list(p_shift_api.search_submissions(after=ep,
                                    sort='asc',
                                    subreddit=subreddit,
                                    filter=['title', 'selftext', 'id'],
                                    limit=100))
        reddit_subs_dn(submissions)
        last_sub_created = submissions[-1].created_utc
        lsc_str = str(last_sub_created)
        with open("logs/time.txt", 'w') as f:
            f.write(lsc_str)
        epochs.append(last_sub_created)
