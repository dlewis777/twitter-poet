import string
import re
cmudict = {}
tweetsent = []
def todict():
	f1 = open('../data/cmudict.txt', 'r+w')
	 
	for line in f1:
		cmudict[line.split()[0]] = line.split()[1:]
	return cmudict


def countSyllables(word):
	syllabeCount = 0
	chars = set('012')
	if word in cmudict:
		for phone in cmudict[word]:
			if any((c in chars) for c in phone):
				syllabeCount += 1
	return syllabeCount


def cutToSize(chunk, size):
	words = tweet.split()
	chunks = []
	head = 0
	tail = 1
	syllables = 0
	while tail <= len(tweet):
		syllables += countSyllables(tweet[tail -1 ])
		if syllables == size:
			chunks.append("".join(tweet[head:tail]))
			head += 1
		if syllables < size:
			tail += 1
			syllables += countSyllables(tweet[tail - 1])
		else:
			head += 1
			syllables -= countSyllables(tweet[head])
	return chunks


def tweet2chunk(tweet):

	#strip links
	tweet = tweet.split('https:')[0]
	words = tweet.split()
	periods = []
	hashtag = []

	for i in range(len(words)):

		if '.' in words[i]:
			periods.append(i)
		if '#' in words[i]:
			hashtag.append(i)	

	if periods:
		for i in periods:
			words[i] = words[i].strip('.')
			temp = words[0:i+1]
			tweetsent.append(' '.join(temp))
			for k in periods:
				if k > i:
					temp = words[i+1:k+1]
					tweetsent.append(' '.join(temp))

		for i in hashtag:
			words[i] = words[i].strip('.')
			temp = words[0:i+1]
			tweetsent.append(' '.join(temp))
			for k in periods:
				if k < i:
					temp = words[k+1: i+1]
					tweetsent.append(' '.join(temp))

	return tweetsent

# Input a string that is equal to the text of a tweet.
# Returns a string of numbers equal to the stresses of the letters
def l2n(chunk, size):

	if len(chunk) < size:

		return None
	elif len(chunk) >= size:

		chunk = chunk[0:size]

	stress = ""

	totalw = []
	for word in chunk.split():
		if '#' in word:
			temp = re.sub(r'[A-Z]',r'\1', word)
			for thing in temp:
				totalw.append(thing)

		else:
			totalw.append(word)
	for word in totalw:


		word = ''.join(e for e in word if e.isalnum())
		word.strip('1234567890')
		word = word.lower()
		if word in cmudict:
			for phone in cmudict[word]:
				stripped = phone.strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			#phone = cmudict[word].strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
				if stripped == "2":
					stripped = "1"
				stress += stripped

	return stress


