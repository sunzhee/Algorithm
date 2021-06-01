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

		
		