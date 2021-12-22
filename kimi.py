import random
import praw
from praw.models import MoreComments
from praw.exceptions import APIException

keywords = ['verstappen', 'hamilton', 'max', 'lewis', 'kimi']

reddit = praw.Reddit(
    user_agent='',
    client_id='',
    client_secret='',
    username='',
    password='',
    ratelimit_seconds=300,
)

subreddits = reddit.subreddit('aarava+tiametmarduk') 

for comment in subreddits.stream.comments(skip_existing=True):
    if isinstance(comment, MoreComments):
        continue

    text = comment.body.lower()

    if comment.author.name == 'kimi-bot':
        continue
    else:
        for keyword in keywords:
            if (keyword in text):
                try:
                    print("\n" + comment.author.name + ": " + comment.body)
                    print('I\'ve just commented: BWOAH')
                    comment.reply('BWOAH')
                except APIException as e:
                    print("Oopsie\n\n" + e.message)