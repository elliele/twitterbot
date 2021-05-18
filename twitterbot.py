# Created by Ellie Le at 5/6/2021

import tweepy
import logging
from config import create_api
import time

# Auto-reply to Mentions Bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    """Respond to user that mentions owner's account."""
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            api.update.status(
                status="Please reach us via DM.",
                in_reply_to_status_id = tweet.id,
            )

    return new_since_id

def respond_hashtags(api, hashtag, since_id):
    """Repond, retweet, and follow to user with certain hashtag."""

    # For loop to iterate over tweets with #CodeNewbie limit to 100
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(100):
        try:
            print("\nFound tweet by: @", tweet.user.screen_name)
            # Enter your personal url
            url = 'xxxxxxxxx'
            message = 'Hello World ' + url
            api.update_status(status = message,
                                in_reply_to_status_id=tweet.id,
                                auto_populate_reply_metadata=True)
            #print('respond to @' + tweet.user.screen_name)

            # Retweet the user
            tweet.retweet()
            print('Retweeted the tweet')
            sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

        # follow user if user is not Followed
        if tweet.user.following == False:
            tweet.user.follow()

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support"], since_id)
        since_id = respond_hashtags(api,'#CodeNewbie', since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()

