import pickle
import rhyme
import stringToNumber
import ballad

f1 = open('8_dt.txt','r+w')
f2 = open('6_dt.txt','r+w')
eight = pickle.load(f1)
six = pickle.load(f2)

stanza = ballad.generate(eight,six,4)

for thing in stanza:

	print thing