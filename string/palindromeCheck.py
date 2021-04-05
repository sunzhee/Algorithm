"""
Palindrome Check
Write a function that takes in a non-empty string and that returns
a boolean representing whether the string is a palindrome.
A palindrome is dened as a string that's written the same
forward and backward. Note that single-character strings are
palindromes.



Sample Input
string = "abcdcba"

Sample Output
true

"""

string = "abcdcba"

#O(n^2) time, O(n) space
#because construct a revers string cost n time, and loop cause n time, total is n^2
def isPalindrome1(string):
	reverseString = ""
	for i in reversed(range(len(string))):
		reverseString += string[i]
	return string == reverseString



#O(n) time, O(n)space
#because we append array, not loop all string to add, so save some time
def isPalindrome2(string):
	reverseString = []
	for i in reversed(range(len(string))):
		reverseString.append(string[i])
	return string == "".join(reverseString)

#recursive solution
#O(n) time, O(n) space
def isPalindrome3(string,i = 0):
	j = len(string) - 1 - i
	if i >= j:
		return True
	else:
		return string[i] == string [j] and isPalindrome(string,i + 1) 

#left right pointer
#O(n) time, O(1) space, it is n/2 time, but ignor /2, so it isO(n) time
def isPalindrome4(string):
	left = 0
	right = len(string) - 1
	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True
		
	