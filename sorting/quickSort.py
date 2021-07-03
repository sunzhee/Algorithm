"""
Quick Sort
Write a function that takes in an array of
integers and returns a sorted version of that
array. Use the Quick Sort algorithm to sort the
array.
If you're unfamiliar with Quick Sort, we
recommend watching the Conceptual
Overview section of this question's video
explanation before starting to code.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]


Sample Output
[2, 3, 5, 5, 6, 8, 9]

"""
# Best: O(n*log(n)) time, O(n*log(n)) space
# Average: O(n*log(n)) time, O(n*log(n)) space
# Worst: O(n ** 2) time, O(n*log(n)) space
def quickSort(array):
	quickSortHelper(array,0,len(array)-1)
	return array

def quickSortHelper(array,startIndex,endIndex):
	if startIndex >= endIndex:
		return
	pivotIndex = startIndex
	leftIndex = startIndex + 1
	rightIndex = endIndex
	
	while rightIndex >= leftIndex:
		# 必须要先判断左右两边和pivot的值，如果符合条件就要立刻交换，然后再左右指针往中间走
		# 快速排序核心算法，有三个关键步骤：
		#  第一，如果左边大于pivot的同时，右边小于pivot那么，左右交换
		#  第二，如果左边小于等于pivot，说明左边在合理位置，那么左边不操作，向中间移动一位 +=1
		#  第三，如果右边大于等于pivot，说明右边在合理位置，右边不操作，向中间移动一位，-=1
		#  全部完成之后，pivot和右边交换
		if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
			swap(leftIndex,rightIndex,array)		
		if array[leftIndex] <= array[pivotIndex]:
			leftIndex += 1
		if array[rightIndex] >= array[pivotIndex]:
			rightIndex -= 1
	swap(rightIndex,pivotIndex,array)
	leftIsSmaller = rightIndex -1 - startIndex < endIndex - (rightIndex + 1)
	if leftIsSmaller:
		quickSortHelper(array,startIndex,rightIndex - 1)
		quickSortHelper(array,rightIndex + 1,endIndex)
	else:
		quickSortHelper(array,rightIndex + 1,endIndex)
		quickSortHelper(array,startIndex,rightIndex - 1)

def swap(i,j,array):
	array[i],array[j] = array[j],array[i]

		
		