"""
Quickselect

Write a function that takes in an array of
distinct integers as well as an integer k and
that returns the kth smallest integer in that
array.
The function should do this in linear time, on
average.


Sample Input
array = [8, 5, 2, 9, 7, 6, 3]
k = 3

Sample Output
5

"""
# average: O(n) time, O(1) space
# 用quick sort的方法，来选择出第n个位置的数字，略微变化
def quickselect(array, k):
	position = k - 1
	return quickSelectHelper(array,0,len(array)-1,position)

def quickSelectHelper(array,startIndex,endIndex,position):
	while True:
		if startIndex > endIndex:
			raise Exception("should never arrive here")
		pivotIndex = startIndex
		leftIndex = startIndex + 1
		rightIndex = endIndex
		# 快速排序的核心部分，如果左边大于pivot同时右边小于pivot，则交换左右
		# 如果左边小于等于pivot，左边位置ok，继续下一个 +=1
		# 如果右边大于等于pivot，右边位置ok,继续下一个 -=1
		# 左坐标大于右坐标，此次循环完成，右坐标和pivot交换位置
		while leftIndex <= rightIndex:
			if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
				swap(leftIndex,rightIndex,array)
			if array[leftIndex] <= array[pivotIndex]:
				leftIndex += 1
			if array[rightIndex] >= array[pivotIndex]:
				rightIndex -= 1
		swap(pivotIndex,rightIndex,array)
		if rightIndex == position:
			return array[rightIndex]
		elif rightIndex < position:
			startIndex = rightIndex + 1
		elif leftIndex > position:
			endIndex = rightIndex - 1
			
def swap(a,b,array):
	array[a],array[b] = array[b],array[a]
		
			
			
