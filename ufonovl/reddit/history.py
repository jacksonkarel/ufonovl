from psaw import PushshiftAPI
import jsonlines
from tqdm import tqdm

from ufonovl.reddit.subreddits import subreddits

def posts_to_json(posts):
    for post in tqdm(posts):
        post.d_.pop("created")
        with jsonlines.open("data/ufos_reddit.jsonl", mode='a') as writer:
            writer.write(post.d_)

def reddit_history():
    p_shift_api = PushshiftAPI()
    for subreddit in tqdm(subreddits):
        # submissions = list(p_shift_api.search_submissions(sort='asc',
        #                             subreddit=subreddit,
        #                             filter=['title', 'selftext', 'subreddit']))
        # posts_to_json(submissions)
        
        comments_gen = p_shift_api.search_comments(sort='asc', subreddit=subreddit, filter=['body', 'subreddit'])
        posts_to_json(comments_gen)
