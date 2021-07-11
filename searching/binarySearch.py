
"""
Binary Search
Write a function that takes in a sorted array of integers as well as
a target integer. The function should use the Binary Search
algorithm to determine if the target integer is contained in the
array and should return its index if it is, otherwise -1 .
If you're unfamiliar with Binary Search, we recommend watching
the Conceptual Overview section of this question's video
explanation before starting to code.


Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

Sample Output
3

"""





#O(logn) Time, O(1) Space
def binarySearch(array, target):
	leftPointer = 0
	rightPointer = len(array) - 1
	while leftPointer <= rightPointer:
		middle = (leftPointer + rightPointer)//2
		portentialMatch = array[middle]
		if portentialMatch == target:
			return middle
		if portentialMatch < target:
			leftPointer = middle + 1
		else:
			rightPointer = middle - 1
	return -1
