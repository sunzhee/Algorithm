"""
Levenshtein Distance

Write a function that takes in two strings and returns the
minimum number of edit operations that need to be performed
on the rst string to obtain the second string.
There are three edit operations: insertion of a character, deletion
of a character, and substitution of a character for another.

Sample Input
str1 = "abc"
str2 = "yabd"

Sample Output
2 // insert "y"; substitute "c" for "d"

"""
str1 = "abc"
str2 = "yabd"


#O(n*m) time | O(n*m) space
def levenshteinDistance(str1, str2):

	# init the 2D array,make sure first row is 0,1,2,3,4...
	edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
	# init the first column to be 0,1,2,3,4...
	for i in range(len(str2) + 1):
		edits[i][0] = i
	# main algo
	for i in range(1,len(str2) + 1):
		for j in range(1,len(str1) + 1):
			if str2[i-1] == str1[j-1]:
				edits[i][j] = edits[i-1][j-1]
			else:
				edits[i][j] = 1 + min(edits[i-1][j],edits[i][j-1],edits[i-1][j-1])
		
	return edits[-1][-1]

print("input:",str1," ",str2)
print("output",levenshteinDistance(str1,str2))