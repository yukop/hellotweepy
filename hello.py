# -*- coding: utf-8 -*-
import tweepy
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open('twitter.conf'))
consumer_token = config.get('Twitter', 'consumer_token')
consumer_secret = config.get('Twitter', 'consumer_secret')
key = config.get('Twitter', 'key')
secret = config.get('Twitter', 'secret')

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.secure = True
auth.set_access_token(key, secret)

api = tweepy.API(auth, secure=True, api_root='/1.1')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
