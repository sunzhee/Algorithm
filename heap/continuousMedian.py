"""
Continuous Median

Write a ContinuousMedianHandler class
that supports:
The continuous insertion of numbers
with the insert method.
The instant (O(1) time) retrieval of the
median of the numbers that have
been inserted thus far with the
getMedian method.
The getMedian method has already been
written for you. You simply have to write the
insert method.
The median of a set of numbers is the
"middle" number when the numbers are
ordered from smallest to greatest. If there's
an odd number of numbers in the set, as in
{1, 3, 7} , the median is the number in
the middle ( 3 in this case); if there's an
even number of numbers in the set, as in
{1, 3, 7, 8} , the median is the average
of the two middle numbers ((3 + 7) / 2 == 5 in this case).


Sample Usage

// All operations below are performed se
ContinuousMedianHandler(): - // ins
insert(5): -
insert(10): -
getMedian(): 7.5
insert(100): -
getMedian(): 10

"""

def MAX_HEAP_FUNC(a,b):
		return a > b
	
def MIN_HEAP_FUNC(a,b):
		return a < b


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC,[])
		self.uppers = Heap(MIN_HEAP_FUNC,[])
        self.median = None

	# 判断插入的数字如果小于lower的最大值，因为lower是max heap，就放进lower
	# 如果大于uppers的最小值，因为uppers是min heap，就放进upper
	# 之后重新平衡两个heap，调整两边最多长度差为1，如果是2以上，则向对方移动一个数字。
	# 返回中间值，如果两个heap长度相等，则peek两个heap顶点，相加除以2
	# 如果两个heap长度差1，则返回长度大的那个顶点
    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
			self.lowers.insert(number)
		else:
			self.uppers.insert(number)
		self.rebalanceHeaps()
		self.updateMedian()
	
	def rebalanceHeaps(self):
		if self.lowers.length - self.uppers.length == 2:
			self.uppers.insert(self.lowers.remove())
		# this is elif, can not use if
		elif self.uppers.length - self.lowers.length == 2:
			self.lowers.insert(self.uppers.remove())

	def updateMedian(self):
		if self.lowers.length == self.uppers.length:
			self.median = (self.lowers.peek() + self.uppers.peek()) / 2
		# here is elif, can not be if
		elif self.lowers.length > self.uppers.length:
			self.median = self.lowers.peek()
		else:
			self.median = self.uppers.peek()
			
    def getMedian(self):
       	return self.median


	
class Heap:
    def __init__(self, comparisonFunc, array):
		self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
		self.length = len(self.heap)
		
    def buildHeap(self, array):
		lastParentIndex = ((len(array) - 1) - 1) // 2
		for index in reversed(range(lastParentIndex + 1)):
			self.siftDown(index,len(array) - 1,array)
		return array
		
    def siftDown(self,startIndex,endIndex,heap):
		childOneIndex = (startIndex*2)+1
		while childOneIndex <= endIndex:
			childTwoIndex = (startIndex*2)+2 if (startIndex*2)+2 <= endIndex else -1
			if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
				indexToChange = childTwoIndex
			else:
				indexToChange = childOneIndex
				
			#if heap[indexToChange] < heap[startIndex]:
			# 上面是min heap class的定义，这个是根据comparisonFunc决定是min heap还是max heap
			if self.comparisonFunc(heap[indexToChange], heap[startIndex]):
				self.swap(startIndex,indexToChange,heap)
				startIndex = indexToChange
				childOneIndex = (startIndex*2)+1
			else:
				break
			

    def siftUp(self,currentIndex,heap):
		directParentIndex = (currentIndex - 1) // 2
		#while  heap[currentIndex] < heap[directParentIndex] and currentIndex > 0:
		# 这里上面是创建min heap，下面是根据comparisonFunc改变成创建min heap或者max heap
		while currentIndex > 0:
			if self.comparisonFunc(heap[currentIndex], heap[directParentIndex]):
				self.swap(currentIndex,directParentIndex,heap)
				currentIndex = directParentIndex
				directParentIndex = (currentIndex - 1) // 2
			else:
				return
			
		

	# O(1) time， O(1) space
    def peek(self):
        return self.heap[0]
	
	# 先把根节点和最后一个节点互换位置，然后pop最后一个节点，同时把新的根节点siftDown到合适位置
	# O(log(n))time,O(1)space
    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        removeValue = self.heap.pop()
		# 更新length属性，删除节点后，长度减1
		self.length -= 1
		self.siftDown(0,len(self.heap)-1,self.heap)
		return removeValue
	
	def insert(self,value):
		self.heap.append(value)
		# 更新length属性，增加节点后，长度加1
		self.length += 1
		self.siftUp(len(self.heap) - 1,self.heap)
		

    def swap(self, i,j,heap):
        heap[i],heap[j] = heap[j],heap[i]
		
