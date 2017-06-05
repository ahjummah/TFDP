import sys
import os
import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# print "here"
consumer_key = 'mwBCusOsQqxdlor3IENlYQXTm'
consumer_secret = 'OCTYVyKf04pUnK8OmXnXpqOD6ROmthisiTCSYB7saIP0q7h4ck'
access_token = '172591183-UPiApsif55xsFGr2ecGRwtGxK9dXYI1SSQ940Xhp'
access_token_secret = 'r3VUelauchouO0JGnTkwXNbHNlUdxQrwKC1WbazvQWM8f'
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
filters = []

# GET https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=2&since_id=14927799pp

def getTweet():

    with open("../Dataset/new-data.csv","a") as f:
        for tweet in tweepy.Cursor(api.search, q= "you ",lang="en").items():
            if not((tweet.text).startswith("RT")):
                if "http" not in tweet.text and "www" not in tweet.text and "https" not in tweet.text:
                    print tweet.text
                    f.write(json.dumps(tweet.text).decode('unicode_escape').encode('ascii','ignore')+'\n')

getTweet();
