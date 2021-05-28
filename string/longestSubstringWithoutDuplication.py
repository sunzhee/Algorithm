"""
Longest Substring Without Duplication

Write a function that takes in a string and
returns its longest substring without duplicate
characters.
You can assume that there will only be one
longest substring without duplication.

Sample Input
string = "clementisacap"

Sample Output
"mentisac

"""
# O(n) time, O(min(n,a)) space
def longestSubstringWithoutDuplication(string):
	seen = {}
	longestSubstring = ""
	startingIndex = 0
	for i,char in enumerate(string):
		if char in seen:
			startingIndex = max(startingIndex,seen[char]+1)
		if len(longestSubstring) < i + 1 - startingIndex:
			longestSubstring = string[startingIndex:i+1]
		seen[char] = i
	return longestSubstring
