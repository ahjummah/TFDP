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
#
# def get_profanitylist():
#     with open('profanity_dictionary.txt','r') as f:
#         for line in f.readlines():
#             filters.append(str(line))
#     for i in range(131,len(filters)):
#         word = (filters[i]).rstrip()
#         getTweet(word)

def getTweet():
    with open("../Evaluating_Dataset/new-data.csv","a") as f:
        for tweet in tweepy.Cursor(api.search,lang="en").items():
            if not((tweet.text).startswith("RT")):
                if "http" not in tweet.text and "www" not in tweet.text and "https" not in tweet.text:
                    print tweet.text
                    f.write(json.dumps(tweet.text).decode('unicode_escape').encode('ascii','ignore')+'\n')

getTweet();
