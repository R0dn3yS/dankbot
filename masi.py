import random
import praw
from praw.models import MoreComments
from praw.exceptions import APIException

quotes = [
    'It\'s called a motor race, okay?',
    'I don\'t access my emails during the races',
    'If you could get back to me within a minute or two, that would be great.',
    'Lapped cars may now overtake.',
    'Go ahead, Jonathan.',
]

reddit = praw.Reddit(
    user_agent='masi-bot',
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

    if comment.author.name == 'masi-bot':
        continue
    elif 'masi' in comment.body.lower() or 'massi' in comment.body.lower():
        try:
            quote = random.choice(quotes)
            print('\n' + comment.author.name + ': ' + comment.body)
            print('I\'ve just commented: ' + quote)
            comment.reply(quote)
        except APIException as e:
            print('Oopsie\n\n' + e.message)
    elif 'sorry?!' in comment.body.lower():
        try:
            quote = 'We went car racing.'
            print('\n' + comment.author.name + ': ' + comment.body)
            print('I\'ve just commented: ' + quote)
            comment.reply(quote)
        except APIException as e:
            print('Oopsie\n\n' + e.message)
