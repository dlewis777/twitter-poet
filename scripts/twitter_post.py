import tweepy
import os
import sys
import ballad
import pickle
import stringToNumber
import rhyme

access_token = os.environ["hophacks_f16_twitter_akey"]
access_secret = os.environ["hophacks_f16_twitter_asecret"]
consumer_key = os.environ["hophacks_f16_twitter_ckey"]
consumer_secret= os.environ["hophacks_f16_twitter_csecret"]
#@realDonaldTrump id is 25073877
#@HillaryClinton id is 1339835893

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

f1 = open('8_dt.txt','r+w')
f2 = open('6_dt.txt','r+w')
eight = pickle.load(f1)
six = pickle.load(f2)

stanza = ballad.generate(eight,six,4)

s = ''
for thing in stanza:

    s += thing + '\n\n'

api.update_status(s)
