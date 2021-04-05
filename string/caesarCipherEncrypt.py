"""
Caesar Cipher Encryptor
Given a non-empty string of lowercase letters and a non-negative
integer representing a key, write a function that returns a new
string obtained by shifting every letter in the input string by k
positions in the alphabet, where k is the key.
Note that letters should "wrap" around the alphabet; in other
words, the letter z shifted by one returns the letter a .


Sample Input
string = "xyz"
key = 2


Sample Output
"zab"

"""

string = "xyz"
key = 2

#O(n) time, O(n) Space
def caesarCipherEncryptor(string, key):
	result = []
	for letter in string:
		result.append(cipherLetter(letter,key))
	#turn an array into a string by joining array to empty string
	return "".join(result)
		
		
def cipherLetter(letter,key):		
	origCode = ord(letter)
	shiftCode = origCode + (key % 26)
	#has to be <= otherwise the last letter z is out of bound
	if shiftCode <= 122:
		resultLetter = chr(shiftCode)
	else:
		resultLetter = chr(96 + (shiftCode % 122))
	return resultLetter

print("input string:",string,"\nkey:",key)
print("output:",caesarCipherEncryptor(string,key))

