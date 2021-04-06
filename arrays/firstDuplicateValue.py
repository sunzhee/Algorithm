"""
First Duplicate Value
Given an array of integers between 1 and n , inclusive, where n is the
length of the array, write a function that returns the rst integer that appears
more than once (when the array is read from left to right).
In other words, out of all the integers that might occur more than once in the
input array, your function should return the one whose rst duplicate value
has the minimum index.
If no integer appears more than once, your function should return -1 .
Note that you're allowed to mutate the input array.


Sample Input #1
array = [2, 1, 5, 2, 3, 3, 4]

Sample Output #1
2 
// 2 is the first integer that appears more than once.
// 3 also appears more than once, but the second 3 appears after second 2



Sample Input #2
array = [2, 1, 5, 3, 3, 2, 4]

Sample Output #2
3 
// 3 is the first integer that appears more than once.
// 2 also appears more than once, but the second 2 appears after second 3

"""

#brutal force
#O(n^2) time, O(1) space
def firstDuplicateValue1(array):
	minID = len(array)
	for i in range(len(array)):
		for j in range(i + 1,len(array)):
			if array[j] == array[i]:
				minID = min(j,minID)
	if minID < len(array):
		return array[minID]
	else:
		return -1

#use a hash tabel to store seen value
#O(n)time, O(n)space
def firstDuplicateValue2(array):
	seen = []
	for i in range(len(array)):
		if array[i] in seen:
			return array[i]
		else:
			seen.append(array[i])
	return -1

#only way and this is not a simple question as it looks
#because "Given an array of integers between 1 and n , inclusive, where n is the length of the array"
#so array id and array value has -1 difference
#for example:
#array value[1,2,3,4,5...n]
#id         [0,1,2,3,4,5...n-1]
#so we can make a 1 to 1 map of id to value, whatever the value stored location, we just use it as a marker
#when we visited the value, we mark it as *= -1, 
#so when we meet the value again, the marker must be already marked as negative value, then we return this value
#important is we need use abs(value) in case the value has marked as negative.

#O(n)time,O(1)space
def firstDuplicateValue(array):
	for i in range(len(array)):
		absValue = abs(array[i])
		if array[absValue - 1] < 0:
			return absValue
		else:
			array[absValue - 1] *= -1
	return -1
