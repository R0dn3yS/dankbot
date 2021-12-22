import random
import praw
from praw.models import MoreComments
from praw.exceptions import APIException

quotes = [
    'Michael I\'ve just sent you an Email, with the diagrams, where the car should be, did you receive that?',
    'You need to reinstate the lap before, it\'s not right',
    'Sorry?!',
    'No, Michael! No, no Michael! That was so not right!',
    'Michael, dis isn\'t right',
    'Michael please no safety car, interferes in the race, please not',
    'No, no Micheal this isn\'t fair',
    'Lewis, you can win this',
    'Fuck em all',
    'Michael blue flags!',
]

reddit = praw.Reddit(
    user_agent='wolff-bot',
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

    if comment.author.name == 'wolff-bot':
        continue
    elif 'it\'s called a motor race, okay?' in comment.body.lower():
        try:
            quote = 'Sorry?!'
            print('\n' + comment.author.name + ': ' + comment.body)
            print('I\'ve just commented: ' + quote)
            comment.reply(quote)
        except APIException as e:
            print('Oopsie\n\n' + e.message)
    elif comment.author.name == 'masi-bot':
        continue
    elif 'wolff' in comment.body.lower() or 'toto' in comment.body.lower():
        try:
            quote = random.choice(quotes)
            print('\n' + comment.author.name + ': ' + comment.body)
            print('I\'ve just commented: ' + quote)
            comment.reply(quote)
        except APIException as e:
            print('Oopsie\n\n' + e.message)
    
