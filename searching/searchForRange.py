"""
Search For Range

Write a function that takes in a sorted array of
integers as well as a target integer. The
function should use a variation of the Binary
Search algorithm to nd a range of indices in
between which the target number is
contained in the array and should return this
range in the form of an array.
The rst number in the output array should
represent the rst index at which the target
number is located, while the second number
should represent the last index at which the
target number is located. The function should
return [-1, -1] if the integer isn't
contained in the array.
If you're unfamiliar with Binary Search, we
recommend watching the Conceptual
Overview section of the Binary Search
question's video explanation before starting
to code.


Sample Input
array = [0, 1, 21, 33, 45, 45, 45, 45, 4
target = 45


Sample Output
[4, 9]

"""

def searchForRange(array, target):
	finialRange = [-1,-1]
	alteredBinarySearch(array,target,0,len(array)-1,finialRange,True)
	alteredBinarySearch(array,target,0,len(array)-1,finialRange,False)
	return finialRange

	

def alteredBinarySearch(array,target,left,right,finialRange,goLeft):
	if left > right:
		return
	mid = (left + right) // 2
	if array[mid] < target:
		# 这里一定要用goLeft传递下去参数，因为这个是决定整体走向是判断左边界还是右边界，这里不能直接写 True or False
		alteredBinarySearch(array,target,mid+1,right,finialRange,goLeft)
	elif array[mid] > target:
		alteredBinarySearch(array,target,left,mid-1,finialRange,goLeft)
	else: # 等于target时候，两种情况
		if goLeft:
			if mid == 0 or array[mid-1] != target:
				finialRange[0] = mid
			else:
				alteredBinarySearch(array,target,left,mid-1,finialRange,goLeft)
		else:
			if mid == len(array)-1 or array[mid+1] != target:
				finialRange[1] = mid
			else:
				alteredBinarySearch(array,target,mid+1,right,finialRange,goLeft)
				
		