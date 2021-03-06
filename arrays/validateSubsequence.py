'''
Validate Subsequence

Given two non-empty arrays of integers, write a
function that determines whether the second
array is a subsequence of the first one.

A subsequence of an array is a set of numbers
that aren't necessarily adjacent in the array but
that are in the same order as they appear in the
array. For instance, the numbers [1, 3, 4]
form a subsequence of the array
[1, 2, 3, 4] , and so do the numbers
[2, 4] . Note that a single number in an
array and the array itself are both valid
subsequences of the array.


Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Sample Output
true

'''

array = array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
	arrId = 0
	seqId = 0
	while arrId < len(array) and seqId < len(sequence):
		if array[arrId] == sequence[seqId]:
			seqId = seqId +1
		arrId = arrId +1
	return seqId == len(sequence)

print("input array:",array)
print("input sequence:",sequence)
print("output:",isValidSubsequence(array,sequence))