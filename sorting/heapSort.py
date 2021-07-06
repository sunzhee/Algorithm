"""
Heap Sort

Write a function that takes in an array of
integers and returns a sorted version of that
array. Use the Heap Sort algorithm to sort
the array.
If you're unfamiliar with Heap Sort, we
recommend watching the Conceptual
Overview section of this question's video
explanation before starting to code.


Sample Input
array = [8, 5, 2, 9, 5, 6, 3]


Sample Output
[2, 3, 5, 5, 6, 8, 9]


"""


# O(n*log(n)) time, O(1) space
def heapSort(array):
	buildMaxHeap(array)
	for endIndex in reversed(range(1,len(array))):
		swap(0,endIndex,array)
		siftDown(0,endIndex-1,array)
	return array
	
def swap(a,b,array):
	array[a],array[b] = array[b],array[a]
	
def buildMaxHeap(array):
	firstParentIndex = (len(array) - 2) // 2
	for currentIndex in reversed(range(firstParentIndex + 1)):
		siftDown(currentIndex,len(array) - 1, array)
		
def siftDown(currentIndex,endIndex,heap):
	childOneIndex = currentIndex * 2 + 1
	while childOneIndex <= endIndex:
		childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
		# 这里要检查child two是否存在，如果是-1表示不存在，那就只能交换child one，这个条件语句反过来不行，会死循环
		if childTwoIndex > -1 and heap[childTwoIndex] > heap[childOneIndex]:
			indexToSwap = childTwoIndex
		else:
			indexToSwap = childOneIndex
		if heap[indexToSwap] > heap[currentIndex]:
			swap(indexToSwap,currentIndex,heap)
			currentIndex = indexToSwap
			childOneIndex = currentIndex * 2 + 1
		else:
			return
			
