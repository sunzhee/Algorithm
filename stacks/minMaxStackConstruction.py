"""
Min Max Stack
Construction
Write a MinMaxStack class for a Min Max
Stack. The class should support:
Pushing and popping values on and o
the stack.
Peeking at the value at the top of the
stack.
Getting both the minimum and the
maximum values in the stack at any
given point in time.
All class methods, when considered
independently, should run in constant time
and with constant space.


Sample Usage
// All operations below are performed sequentially 

MinMaxStack(): - // instantiate a MinMaxStack
push(5): -
getMin(): 5
getMax(): 5
peek(): 5
push(7): -
getMin(): 5
getMax(): 7
peek(): 7
push(2): -
getMin(): 2
getMax(): 7
peek(): 2
pop(): 2
pop(): 7
getMin(): 5
getMax(): 5
peek(): 5


"""

# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		# 用建立的minMaxStack数组保存每一次push进来新数值之后的min max值，这样可以保证O(1)时间执行getMin() getMax()
		# 注意在pop以后，minMaxStack也要pop掉一个
		self.minMaxStack = []
		self.stack = []
		
    def peek(self):
		return self.stack[len(self.stack) - 1]

    def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()

    def push(self, number):
		# 建立一个字典，有两个key值min max,对应两个数字,然后将这个字典加入到minMaxStack数组中
		# 例: minMaxStack: [{'min': 5, 'max': 5}, {'min': 2, 'max': 5}, {'min': 2, 'max': 7}]
		#     stack: [5, 2, 7]
		newMinMax = {"min":number,"max":number}
		if len(self.minMaxStack) != 0:
			lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
			newMinMax["min"] = min(lastMinMax["min"],number)
			newMinMax["max"] = max(lastMinMax["max"],number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

    def getMin(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
		return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


	
abc = MinMaxStack()
abc.push(5)
abc.push(2)
abc.push(7)

print(abc.minMaxStack)
print(abc.stack)

"""
test cases
        stack = program.MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)
"""