import tweepy
import os

access_token = os.environ["twitter_akey"]
access_secret = os.environ["twitter_asecret"]
consumer_key = os.environ["twitter_ckey"]
consumer_secret= os.environ["twitter_csecret"]
#@realDonaldTrump id is 25073877

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(id = '25073877', count = 100, include_rts = False)

for status in stuff:
    print status.text + "\n"
