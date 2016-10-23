import rhyme
import random
#n is number of stanza
# eight is list of 8 sylable phrases
# six is list of 6 sylable phrases
def generate(eight, six, n):

	eightrhyme = rhyme.find_rhyme(eight)
	sixrhyme = rhyme.find_rhyme(six)

	tempe = eightrhyme
	temps = eightrhyme
	stanza = []
	for i in range(n):
		l1 = random.choice(tempe.keys())
		if l1 in tempe:
			tempe.pop(l1)
		l2 = random.choice(temps.keys())
		if l2 in temps:
			temps.pop(l2)
		for key in temps.keys():
			if l2 in temps[key]:
				temps[key].remove(l2)
		l3 = random.choice(tempe.keys())
		if l3 in tempe:
			tempe.pop(l3)
		l4 = random.choice(l2)
		if l4 in temps:
			temps.pop(l4)
		for key in temps.keys():
			if l4 in temps[key]:
				temps[key].remove(l4)

		s = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
		stanza.append(s)

	return stanza