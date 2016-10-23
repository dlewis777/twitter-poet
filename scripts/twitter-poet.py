import sys
import argparse
import matcher
import stringToNumber
import ballad
import pickle

def checkArgs(parser):
	if not parser.meter.upper() in matcher.METERS:
		print "Not a valid meter"
		return False
	return True


def makeArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('--tweet-file', type=str, required=True, help="File containing tweets to choose from")
	parser.add_argument("--meter", type=str, required=False, help="The meter for the poem, e.g. iambic")
	parser.add_argument("--num-lines", type=int, required=False, help="the length of the poem in lines")
	parser.add_argument("--form", type=str, required=True, help="form of the poem")
	parser.add_argument("--num-poems", type=int, required=True, help="number of poems")
	parser.add_argument("--save-file", type=str, required=False, help="file to save tetra,tri in", default=None)
	parser.add_argument("--load-file", type=str, required=False, help="file to load tetra, tri from", default=None)
	
	args = parser.parse_args()
	#if not checkArgs(args):
	#	exit(1)
	return args


def getOfMeter(meter, tweets):
	pattern = matcher.Matcher(meter)
	valid_chunks = set()
	i = 0
	for tweet in tweets:
		chunks = stringToNumber.tweet2chunk(tweet)
		for chunk in chunks:
			subchunks = stringToNumber.cutToSize(chunk, pattern.getSyllableCount())
			for subchunk in subchunks:
				if pattern.matches(stringToNumber.l2n(subchunk)):
					if not subchunk in valid_chunks:
						valid_chunks.add(subchunk)	
		i += 1
		if i%50 == 0 :
			print i
	return list(valid_chunks)

def generateBallad(tweets, times, save_file=None):
	tetra = getOfMeter(matcher.METERS["IAMBIC_TETRAMETER"], tweets)
	tri = getOfMeter(matcher.METERS["IAMBIC_TRIMETER"], tweets)
	if not save_file == None:
		pickle.dump[(tetra, tri), save_file]
	ballads = []
	for _ in range(times):
		ballads.append(ballad.generate(tetra, tri, 4))
	return ballads

def generatePoem(tweets, form, num, save_file=None):
	if form.lower() == "ballad":
		return generateBallad(tweets, num)
	else:
		return

def genBalladFromLoad(loadfile, times):
	itemlist = pickle.load(loadfile)
	tetra = itemlist[0]
	tri = itemlist[1]
	ballads = []
	for _ in range(times):
		ballads.append(ballad.generate(tetra, tri, 4))
	return ballads


def main():
	tweets = []
	stringToNumber.todict()
	parser = makeArgs()
	i = 0
	if parser.load_file == None:
		with open(parser.tweet_file, 'r') as tweet_file:
			for line in tweet_file:
				line = line.strip()
				if len(line) == 0:
					continue
				tweets.append(line)
				i += 1
				if i > parser.num_lines:
					break

		generatePoem(tweets, parser.form, parser.num_poems, parser.save_file)
			#print " ".join(poem)
	else:
		genBalladFromLoad(parser.load_file)





if __name__ == '__main__':
	main()