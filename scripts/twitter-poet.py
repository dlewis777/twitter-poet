import sys
import argparse
import matcher
import stringToNumber
import ballad

def checkArgs(parser):
	if not parser.meter.upper() in matcher.METERS:
		print "Not a valid meter"
		return False
	return True


def makeArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('--tweet-file', type=str, required=True, help="File containing tweets to choose from")
	parser.add_argument("--meter", type=str, required=False, help="The meter for the poem, e.g. iambic")
	parser.add_argument("--num-lines", type=str, required=False, help="the length of the poem in lines")
	parser.add_argument("--form", type=str, required=True, help="form of the poem")
	args = parser.parse_args()
	#if not checkArgs(args):
	#	exit(1)
	return args


def getOfMeter(meter, tweets):
	pattern = matcher.Matcher(meter)
	valid_chunks = set()
	for tweet in tweets:
		chunks = stringToNumber.tweet2chunk(tweet)
		for chunk in chunks:
			subchunks = stringToNumber.cutToSize(chunk, pattern.getSyllableCount())
			for subchunk in subchunks:
				if pattern.matches(stringToNumber.l2n(subchunk)):
					if not subchunk in valid_chunks:
						valid_chunks.add(subchunk)	
	return list(valid_chunks)

def generateBallad(tweets):
	tetra = getOfMeter(matcher.METERS["IAMBIC_TETRAMETER"], tweets)
	tri = getOfMeter(matcher.METERS["IAMBIC_TRIMETER"], tweets)
	#print tetra
	#print tri
	balladLines = ballad.generate(tetra, tri, 4)
	return balladLines[0]

def generatePoem(tweets, form):
	if form.lower() == "ballad":
		return generateBallad(tweets)
	else:
		return


def main():
	tweets = []
	stringToNumber.todict()
	parser = makeArgs()
	with open(parser.tweet_file, 'r') as tweet_file:
		for line in tweet_file:
			line = line.strip()
			tweets.append(line)

	print generatePoem(tweets, parser.form)





if __name__ == '__main__':
	main()