import tweepy
import os
import sys

access_token = os.environ["twitter_akey"]
access_secret = os.environ["twitter_asecret"]
consumer_key = os.environ["twitter_ckey"]
consumer_secret= os.environ["twitter_csecret"]
#@realDonaldTrump id is 25073877
#@HillaryClinton id is 1339835893

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(id = sys.argv[1], count = sys.argv[2], include_rts = False)

for status in stuff:
    print status.text.encode('ascii', 'ignore')
