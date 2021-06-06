# Twitter Bot

A twitter bot program that automatically that query for specific keyword and retweet to user.

## Tweepy: Twitter for Python

### Installation
```
pip install tweepy
```

### How Tweepy API works
```
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
 ```
 ### Documentation
 <ul>
  <li>https://docs.tweepy.org/en/latest/api.html</li>
  <li>https://developer.twitter.com/en/apply-for-access</li>
  </ul>

 Note: Python 3.6 - 3.9 are supported.
