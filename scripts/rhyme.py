import stringToNumber as s2n
# only input of size 6
cmudict = {}
rhymdict = {}
vowels = ['AH0', 'IH2', 'EY1', 'AA1', 'ER0', 'EH0', 'AO2', 'AA0',
			'EH1', 'AA2','IY2','AE1', 'OW2', 'IY0', 'IY0', 'IH0',
			'AE2','OW1','OW0','EY0','AW2', 'AW1', 'UW1','IY1','EY2',
			'UW0','EH2','AE0', 'AH1','AH2','UW2','AO0','AO1','AY1',
			'IH1','AY2','ER1','UH1','OY2','AY0','OY1','UH2','ER2',
			'OY0','UH0','AW0']

def find_rhyme(correct):

	cmudict = s2n.todict()
	
	for sentence in correct:

		rhymdict[sentence] = []

		final = sentence.split()[-1]
		syl = cmudict[final]
		
		finalsyl = ''
		ending = []
		for x in reversed(syl):
			if x in vowels:
				finalsyl = x.strip('012')
				ending.append(finalsyl)
				break
			else:
				ending.append(x)
		for other in correct:

			if other is not sentence:

				otherfinal = other.split()[-1]
				print(otherfinal)
				ofp = cmudict[otherfinal]
				othersyl = ''
				ending2 = []
				for y in reversed(ofp):
					if y in vowels:
						othersyl = y.strip('012')
						ending2.append(othersyl)
						break
					else:
						ending2.append(y)

				if ' '.join(ending2) == ' '.join(ending):

					rhymdict[sentence].append(other)

	return rhymdict

if __name__ == '__main__':
	
	stuff = ['a cat', 'a bat','we pant', 'there is a slant']
	k = find_rhyme(stuff)
	print(k)
