"""
Min Heap Construction
Implement a MinHeap class that supports:
Building a Min Heap from an input array of integers.
Inserting integers in the heap.
Removing the heap's minimum / root value.
Peeking at the heap's minimum / root value.
Sifting integers up and down the heap, which is to be used when inserting and
removing values.
Note that the heap should be represented in the form of an array.
If you're unfamiliar with Min Heaps, we recommend watching the Conceptual
Overview section of this question's video explanation before starting to code.


Sample Usage
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
// All operations below are performed sequentially.

MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap 
buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
peek(): -5
remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
peek(): 2
remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
peek(): 6
insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
"""


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
	def __init__(self, array):
		# Do not edit the line below.
		self.heap = self.buildHeap(array)
		
	# O(n)time , O(1)space
	# 整个heap处于乱序状态，在数组中找出最后一个含有子节点的父节点index，和数组最大index进行siftDown操作， 直到找到合适位置为止。
	# 然后循环倒数第二个父节点往下siftDown操作，把所有父节点都走一遍，即是一个标准heap了
	# 注意循环是rebersed，
	def buildHeap(self, array):
		# 最后一个含有子节点的父节点，用array长度len(array)-1，套用公式，(index值 -1)//2 round down取整
		lastParentIndex = ((len(array) - 1) - 1) // 2
		for index in reversed(range(lastParentIndex + 1)):
			self.siftDown(index,len(array) - 1,array)
		return array
		
	
	# 两个子节点，(currentIndex * 2) + 1和(currentIndex * 2) +2
	# 将起始index移动到结束index之间的适合位置，主要是为了remove调用
	# O(log(n)) time, O(1) space
	def siftDown(self,startIndex,endIndex,heap):
		childOneIndex = (startIndex*2)+1
		# 这里为什么用 <= ?
		while childOneIndex <= endIndex:
			childTwoIndex = (startIndex*2)+2 if (startIndex*2)+2 <= endIndex else -1
			# 如果第二个子节点超过endIndex的话，给第二个子节点index值暂定-1
			# 这里比较巧妙，如果第二子节点不是-1，并且第二个子节点比第一个子节点值小，
			# 那么等待交换的子节点必然是第二个，否则等待交换的必然是第一个子节点
			#（如果第二子结点为-1，那么等待交换的也必然是第一个子节点）
			if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
				indexToChange = childTwoIndex
			else:
				indexToChange = childOneIndex
				
			if heap[indexToChange] < heap[startIndex]:
				self.swap(startIndex,indexToChange,heap)
				startIndex = indexToChange
				childOneIndex = (startIndex*2)+1
			# 如果已经值大于或者等于子节点了，即else这里，直接跳出循环结束
			else:
				break
			

	# 把指定位置的index值向上移动到合适的位置，主要是为了insert调用
	# 先计算当前父节点值，(index - 1)//2 round down取整，既是父节点
	# 循环到根节点或者父节点小于当前值为止。
	# currentIndex > 0 再交换下去就是根节点，currentIndex=0，无需操作，跳出循环
	# O(log(n)) time, O(1) space
	def siftUp(self,currentIndex,heap):
		directParentIndex = (currentIndex - 1) // 2
		while  heap[currentIndex] < heap[directParentIndex] and currentIndex > 0:
			self.swap(currentIndex,directParentIndex,heap)
			currentIndex = directParentIndex
			directParentIndex = (currentIndex - 1) // 2
		


	# O(1) time， O(1) space
	def peek(self):
		return self.heap[0]
	
	# 先把根节点和最后一个节点互换位置，然后pop最后一个节点，同时把新的根节点siftDown到合适位置
	# O(log(n))time,O(1)space
	def remove(self):
		self.swap(0,len(self.heap)-1,self.heap)
		removeValue = self.heap.pop()
		self.siftDown(0,len(self.heap)-1,self.heap)
		return removeValue
	
	# O(log(n))time,O(1)space
	# 先把值加入到最后一个节点，然后siftUp到合适的位置
	def insert(self,value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1,self.heap)
		
	# O(1) time, O(1) space
	# 交换两个节点值，i,j是index
	def swap(self, i,j,heap):
		heap[i],heap[j] = heap[j],heap[i]
