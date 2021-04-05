"""
First Non-Repeating Character

Write a function that takes in a string of lowercase Englishalphabet letters and returns the index of the string's rst nonrepeating character.
The rst non-repeating character is the rst character in a string
that occurs only once.
If the input string doesn't have any non-repeating characters,
your function should return -1 .



Sample Input
string = "abcdcaf"


Sample Output
1


"""






string = "abcdcaf"





def firstNonRepeatingCharacter1(string):
	for id1 in range(len(string)):
		isReapting = False
		for id2 in range(len(string)):
			if string[id1] == string[id2] and id1 != id2:
				isReapting = True
		
		if not isReapting:
			return id1
		
	return -1


#O(n) time, O(1) space, because the hash map has maximun 26 characters
def firstNonRepeatingCharacter(string):
	charFreq = {}
	
	for char in string:
		#this is a dict function to get char value
		charFreq[char] = charFreq.get(char,0) + 1
		
	for id1 in range(len(string)):
		if charFreq[string[id1]] == 1:
			return id1
	
	return -1

print("input:",string)
print("output:",firstNonRepeatingCharacter(string))