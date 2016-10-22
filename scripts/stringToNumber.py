import string
cmudict = {}

def todict(file):
	f1 = open('cmudict.txt', 'r+w')
	 
	 for line in f1:
	 	cmudict[line.split()[0]] = line.split()[1]

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
	

