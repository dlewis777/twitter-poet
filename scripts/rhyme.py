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

		final = sentence[-1]
		syl = cmudict[final]
		finalsyl = ''
		for x in reversed(syl):
			if x in vowels:
				finalsyl = x.strip('012')
				break

		for other in correct:

			if other is not sentence:

				otherfinal = other[-1]
				othersyl = ''
				for y in reversed(otherfinal):
					if y in vowels:
						othersyl = y.strip('012')

				if finalsyl is othersyl:

					rhymdict[sentence].append(other)

	return rhymdict


