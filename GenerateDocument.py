"""
Generate Document


You're given a string of available characters and a string
representing a document that you need to generate. Write a
function that determines if you can generate the document using
the available characters. If you can generate the document, your
function should return true ; otherwise, it should return
false .
You're only able to generate the document if the frequency of
unique characters in the characters string is greater than or
equal to the frequency of unique characters in the document
string. For example, if you're given characters = "abcabc"
and document = "aabbccc" you cannot generate the
document because you're missing one c .
The document that you need to create may contain any
characters, including special characters, capital letters, numbers,
and spaces.
Note: you can always generate the empty string ( "" ).


Sample Input
characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

Sample Output
true


"""



def generateDocument(characters, document):
	for char in document:
		charFrequncy = getCharFreq(char,characters)
		docFrequncy = getCharFreq(char,document)
		if charFrequncy < docFrequncy:
			return False
	return True

def getCharFreq(char,document):
	charFreq = 0
	for i in document:
		if i == char:
			charFreq += 1
	return charFreq


def generateDocument(characters, document):
	alreadyCounted = []
	for char in document:
		if char not in alreadyCounted:
			charFrequncy = getCharFreq(char,characters)
			docFrequncy = getCharFreq(char,document)
			if charFrequncy < docFrequncy:
				return False
			alreadyCounted.append(char)
	return True

def getCharFreq(char,document):
	charFreq = 0
	for i in document:
		if i == char:
			charFreq += 1
	return charFreq


def generateDocument(characters, document):
	charSet = {}
	for i in characters:
		if i in charSet:
			charSet[i] += 1
		else:
			charSet[i] = 1
	
	for j in document:
		if j not in charSet:
			return False
		else:
			charSet[j] -= 1
		if charSet[j] < 0:
			return False
		
	return True
