import rhyme
import random

def generate(eight, six):

	eightrhyme = rhyme.find_rhyme(eight)
	sixrhyme = rhyme.find_rhyme(six)

	tempe = eightrhyme
	temps = eightrhyme
	stanza = []
	for i in range(4):
		l1 = random.choice(tempe.keys())
		tempe.remove(l1)
		l2 = random.choice(temps.keys())
		temps.remove(l2)
		for key in temps.keys():
			if l2 in temps[key]:
				temps[key].remove(l2)
		l3 = random.choice(tempe.keys())
		tempe.remove(l3)
		l4 = random.choice(l2)
		temps.remove(l4)
		for key in temps.keys():
			if l4 in temps[key]:
				temps[key].remove(l4)

		s = l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
		stanza.append(s)

	return stanza