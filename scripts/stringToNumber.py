import string
cmudict = {}
tweetsent = []
def todict():
	f1 = open('../data/cmudict.txt', 'r+w')
	 
	for line in f1:
		cmudict[line.split()[0]] = line.split()[1:]

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
	for word in chunk.split():
		''.join(e for e in word if e.isalnum())
		word.strip('1234567890')
		if cmudict[word] != None:
			phone = cmudict[word].strip('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			stress += phone

	return stress


