import re

IAMBIC = "01"
TROCHAIC = "10"
SPONDAIC = "11"
ANAPESTIC = "001"
DACTYLIC = "100"
IAMBIC_PENTAMETER = IAMBIC * 5
TROCHAIC_TETRAMETER = TROCHAIC *4
ANAPESTIC_TRIMETER = ANAPESTIC*3
DACTYLIC_HEXAMETER = DACTYLIC*5 + TROCHAIC



class Matcher():

	def __init__(self, pattern):
		self.pattern = re.compile(pattern)

	def matches(self, string):
		matched = self.pattern.match(string)
		return matched.start() - matched.end() == len(string):

	def findMatch(self, string):
		return (matched.start(), matched.end())
		
	
		




