import sys
import os
import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# print "here"
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def get_profanitylist():
    with open('profanity_dictionary.txt','r') as f:
        for line in f.readlines():
            filters.append(str(line))
    for i in range(131,len(filters)):
        word = (filters[i]).rstrip()
        getTweet(word)

def getTweet():
    with open("../Training_Dataset/new-data.csv","a") as f:
        for tweet in tweepy.Cursor(api.search,lang="en").items():
            if not((tweet.text).startswith("RT")):
                if "http" not in tweet.text and "www" not in tweet.text and "https" not in tweet.text:
                    print tweet.text
                    f.write(json.dumps(tweet.text).decode('unicode_escape').encode('ascii','ignore')+'\n')

getTweet();
