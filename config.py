# Created by Ellie Le at 5/10/2021

import tweepy
import logging
import os

from keys import keys


logger = logging.getLogger()

def create_api():
    api_key = os.getenv(keys['api_key'])
    api_secret = os.getenv(keys['api_secret_key'])
    access_token = os.getenv(keys['access_token'])
    access_token_secret = os.getenv(keys['access_token_secret'])

    auth = tweepy.OAuthHandler(keys['api_key'], keys['api_secret_key'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api
