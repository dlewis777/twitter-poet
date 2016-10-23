import string
import re
cmudict = {}
tweetsent = []
def todict():
	f1 = open('cmudict.txt', 'r+w')
	 
	for line in f1:
		cmudict[line.split()[0]] = line.split()[1:]
	return cmudict


def countSyllables(word):
	word = word.lower()
	syllabeCount = 0
	chars = set('012')
	if word in cmudict:
		for phone in cmudict[word]:
			if any((c in chars) for c in phone):
				syllabeCount += 1
	return syllabeCount


def cutToSize(chunk, size):
	words = chunk.split()
	chunks = []
	head = 0
	tail = 0
	syllables = 0
	#print words
	while max(head, tail) < len(words):
		#print "head: " + str(head) +" tail: " + str(tail) + " syllables: " + str(syllables) + " desired: " + str(size)
		if syllables == size:
			chunks.append(" ".join(words[head:tail]))
			syllables -= countSyllables(words[head])
			head += 1
		if syllables < size:
		#	print "added: " + words[tail] + " size: " + str(countSyllables(words[tail]))
			syllables += countSyllables(words[tail])
			tail += 1
		else:
		#	print "removed: " + words[head] + " size: " + str(countSyllables(words[head]))
			syllables -= countSyllables(words[head])
			head += 1
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
def l2n(chunk):

	stress = ""

	totalw = []
	for word in chunk.split():
		if '#' in word:
			pat = re.compile('([A-Z])')
			temp = pat.sub(r' \1', word).strip()
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


