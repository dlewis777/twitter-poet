import sys
import argparse
import matcher
import stringToNumber

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
	args = parser.parse_args()
	if not checkArgs(args):
		exit(1)
	return args



def main():
	#patterns = ["0101010101"]
	#pattern = matcher.Matcher(matcher.METERS["IAMBIC_PENTAMETER"])
	#print pattern.matches(patterns[0])
	tweets = []
	stringToNumber.todict()
	parser = makeArgs()
	with open(parser.tweet_file, 'r') as tweet_file:
		for line in tweet_file:
			line = line.strip()
			tweets.append(line)
	pattern = matcher.Matcher(matcher.METERS[parser.meter.upper()])
	valid_chunks = []
	for tweet in tweets:
		chunks = stringToNumber.tweet2chunk(tweet)
		#print tweet
		#print chunks
		#print ""
		for chunk in chunks:
			subchunks = stringToNumber.cutToSize(chunk, pattern.getSyllableCount())
			for subchunk in subchunks:
				if pattern.matches(stringToNumber.l2n(subchunk)):
					valid_chunks.append(chunk)
			#print chunk + " : " + stringToNumber.l2n(chunk)
		#print ""

	print valid_chunks





if __name__ == '__main__':
	main()