import requests

from ufonovl.reddit.subreddits import subreddits

def subreddits_total():
    post_type = "comment"
    total_posts = 0
    for subreddit in subreddits:
        p_shift_url = f'https://api.pushshift.io/reddit/search/{post_type}'
        payload = {
            'size': '0',
            'metadata': 'true', 
            "subreddit": subreddit,
        }
        sub_data = requests.get(p_shift_url, params=payload)
        sub_tot = sub_data.json()['metadata']['total_results']
        total_posts += sub_tot 
    print(total_posts)