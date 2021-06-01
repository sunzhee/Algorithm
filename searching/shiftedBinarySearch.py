"""
Shifted Binary Search

Write a function that takes in a sorted array of
distinct integers as well as a target integer.
The caveat is that the integers in the array
have been shifted by some amount; in other
words, they've been moved to the left or to
the right by one or more positions. For
example, [1, 2, 3, 4] might have turned
into [3, 4, 1, 2] .
The function should use a variation of the
Binary Search algorithm to determine if the
target integer is contained in the array and
should return its index if it is, otherwise -1 .
If you're unfamiliar with Binary Search, we
recommend watching the Conceptual
Overview section of the Binary Search
question's video explanation before starting
to code.



Sample Input
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33

Sample Output
8
"""


# O(log(n)) time, O(log(n)) space
# 递归方法，比较直观
def shiftedBinarySearch(array, target):
	return shiftedBinarySearchHelper(array,target,0,len(array)-1)

def shiftedBinarySearchHelper(array,target,left,right):
	# base case 1, 走完了还没找到，返回-1
	if left > right:
		return -1
	middle = (left + right) // 2
	middleNumber = array[middle]
	leftNumber = array[left]
	rightNumber = array[right]
	if target == middleNumber:
		return middle
	elif leftNumber <= middleNumber:
		if target < middleNumber and target >= leftNumber:
			# 说明在左边
			return shiftedBinarySearchHelper(array,target,left,middle - 1)
		else:
			# 否则说明在右边
			return shiftedBinarySearchHelper(array,target,middle + 1,right)
	else:
		if target > middleNumber and target <= rightNumber:
			return shiftedBinarySearchHelper(array,target,middle + 1,right)
		else:
			return shiftedBinarySearchHelper(array,target,left,middle - 1)
		


# O(log(n)) time, O(1) space
# while的方法，省空间
def shiftedBinarySearch(array, target):
	return shiftedBinarySearchHelper(array,target,0,len(array)-1)

def shiftedBinarySearchHelper(array,target,left,right):
	# base case 1, 走完了还没找到，返回-1
	while left <= right:
		middle = (left + right) // 2
		middleNumber = array[middle]
		leftNumber = array[left]
		rightNumber = array[right]
		if target == middleNumber:
			return middle
		elif leftNumber <= middleNumber:
			if target < middleNumber and target >= leftNumber:
				# 说明在左边
				right = middle - 1
			else:
				# 否则说明在右边
				left = middle + 1
		else:
			if target > middleNumber and target <= rightNumber:
				left = middle + 1
			else:
				right = middle - 1
	return -1
