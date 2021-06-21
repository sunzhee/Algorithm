"""
Sort K-Sorted Array
Write a function that takes in a non-negative
integer k and a k-sorted array of integers and
returns the sorted version of the array. Your
function can either sort the array in place or
create an entirely new array.
A k-sorted array is a partially sorted array in
which all elements are at most k positions
away from their sorted position. For example,
the array [3, 1, 2, 2] is k-sorted with
k = 3 , because each element in the array is
at most 3 positions away from its sorted
position.
Note that you're expected to come up with an
algorithm that can sort the k-sorted array
faster than in O(nlog(n)) time.


Sample Input
array = [3, 2, 1, 5, 4, 7, 6, 5]
k = 3

Sample Output
[1, 2, 3, 4, 5, 5, 6, 7]


"""

# O(n*log(k)) time , O(k) space
# 应该是 n*log(k) + k, 因为k<= n，所以可以替换为，n*log(k) + n = n*(log(k)+1)，所以n*log(k)
# 每次把k+1个数字放进minHeap里面，从这k+1的heap里找出最小值放在最左边，直到排序完成
def sortKSortedArray(array, k):
	minHeapWithKElement = MinHeap(array[:min(k+1,len(array))])
	nextIndexToInsertElement = 0
	for idx in range(k+1,len(array)):
		minElement = minHeapWithKElement.remove()
		array[nextIndexToInsertElement] = minElement
		nextIndexToInsertElement += 1
		
		currentElement = array[idx]
		minHeapWithKElement.insert(currentElement)
	
	while not minHeapWithKElement.isEmpty():
		minElement = minHeapWithKElement.remove()
		array[nextIndexToInsertElement] = minElement
		nextIndexToInsertElement += 1
		
	return array

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
		
    def buildHeap(self, array):
		lastParentIndex = ((len(array) - 1) - 1) // 2
		for index in reversed(range(lastParentIndex + 1)):
			self.siftDown(index,len(array) - 1,array)
		return array
	
	def isEmpty(self):
		return True if len(self.heap) == 0 else False
		
	def siftDown(self,startIndex,endIndex,heap):
		childOneIndex = (startIndex*2)+1
		while childOneIndex <= endIndex:
			childTwoIndex = (startIndex*2)+2 if (startIndex*2)+2 <= endIndex else -1
			if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
				indexToChange = childTwoIndex
			else:
				indexToChange = childOneIndex
				
			if heap[indexToChange] < heap[startIndex]:
				self.swap(startIndex,indexToChange,heap)
				startIndex = indexToChange
				childOneIndex = (startIndex*2)+1
			else:
				break
			
    def siftUp(self,currentIndex,heap):
		directParentIndex = (currentIndex - 1) // 2
		while  heap[currentIndex] < heap[directParentIndex] and currentIndex > 0:
			self.swap(currentIndex,directParentIndex,heap)
			currentIndex = directParentIndex
			directParentIndex = (currentIndex - 1) // 2
		
    def peek(self):
        return self.heap[0]
	
    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        removeValue = self.heap.pop()
		self.siftDown(0,len(self.heap)-1,self.heap)
		return removeValue
	
	def insert(self,value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1,self.heap)
		
    def swap(self, i,j,heap):
        heap[i],heap[j] = heap[j],heap[i]
		
		
		
		
