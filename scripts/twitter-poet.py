import sys
import argparse
import matcher


def checkArgs(parser):
	if not parser.meter.upper() in matcher.METERS:
		print "Not a valid meter"
		return False
	return True


def makeArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('--tweet-file', type=str, required=True, help="File containing tweets to choose from")
	parser.add_argument("--meter", type=str, required=True, help="The meter for the poem, e.g. iambic")
	parser.add_argument("--num-lines", type=str, required=True, help="the length of the poem in lines")

	if not checkArgs(parser):
		exit(1)
	return parser



def main():
	tweets = []
	parser = makeArgs()
	with open(parser.tweet_file, 'r') as tweet_file:
		for line in tweet_file:
			line = line.strip()
			tweets.append(line)
	





if __name__ == '__main__':
	main()