import tweepy
import os
import sys

access_token = os.environ["hophacks_f16_twitter_akey"]
access_secret = os.environ["hophacks_f16_twitter_asecret"]
consumer_key = os.environ["hophacks_f16_twitter_ckey"]
consumer_secret= os.environ["hophacks_f16_twitter_csecret"]
#@realDonaldTrump id is 25073877
#@HillaryClinton id is 1339835893

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
new_tweets = api.user_timeline(id = sys.argv[1], count = 200, include_rts = False)
while len(new_tweets) > 0:
	for tweet in new_tweets:
		print tweet.text.encode('ascii', 'ignore') + "\n"
	oldest = new_tweets[-1].id - 1
	new_tweets = api.user_timeline(id = sys.argv[1], count=200, max_id = oldest, include_rts=False)


#api.update_status('roses are red\nviolets are blue\nyou smell like a pumpkin\nand a smelly old shoe')
