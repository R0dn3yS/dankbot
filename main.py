import random
import praw
from praw.models import MoreComments
from praw.exceptions import APIException

totoQuotes = [
    "Michael I've just sent you an Email, with the diagrams, where the car should be, did you receive that?",
    "You need to reinstate the lap before, it's not right",
    "Sorry?!",
    "No, Michael! No, no Michael! That was so not right!",
    "Michael, dis isn't right",
    "Michael please no safety car, interferes in the race, please not",
    "No, no Michael this isn't fair",
    "Lewis, you can win this",
    "Fuck em all",
    "Michael blue flags!",
]

michaelQuotes = [
    "It's called a motor race, okay?",
    "I don't access my emails during the races",
    "If you could get back to me within a minute or two, that would be great.",
    "Lapped cars may now overtake.",
    "Go ahead, Jonathan.",
]

reddit = praw.Reddit(
    user_agent="",
    client_id="",
    client_secret="",
    username="",
    password="",
    ratelimit_seconds=300,
)

subreddits = reddit.subreddit("aarava+tiametmarduk") 

for comment in subreddit.stream.comments(skip_existing=True):
    if isinstance(comment, MoreComments):
        continue

    text = comment.body.lower()

    if comment.author.name == "R0dn3yS":
        continue
    elif "masi" in text or "massi" in text or "michael" in text:
        try:
            quote = random.choice(michaelQuotes)
            print("\n" + comment.author.name + ": " + comment.body)
            print("I've just commented: " + quote)
            comment.reply(quote)
        except: 
            print("Oopsie woopsie")
    elif "it's called a motor race, okay?" in comment.body.lower():
        try:
            quote = "Sorry?!"
            print("\n" + comment.author.name + ": " + comment.body)
            print("I've just commented: " + quote)
            comment.reply(quote)
        except APIException as e:
            print("Oopsie\n\n" + e.message)
    elif comment.author.name == "wolff-bot" or comment.author.name == "masi-bot":
        continue
    elif "wolff" in text or "toto" in text:
        try:
            quote = random.choice(totoQuotes)
            print("\n" + comment.author.name + ": " + comment.body)
            print("I've just commented: " + quote)
            comment.reply(quote)
        except APIException as e:
            print("Oopsie\n\n" + e.message)
