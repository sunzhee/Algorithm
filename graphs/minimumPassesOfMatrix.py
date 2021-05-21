"""
Minimum Passes Of Matrix

Write a function that takes in an integer
matrix of potentially unequal height and
width and returns the minimum number of
passes required to convert all negative
integers in the matrix to positive integers.
A negative integer in the matrix can only be
converted to a positive integer if one or
more of its adjacent elements is positive. An
adjacent element is an element that is to the
left, to the right, above, or below the current
element in the matrix. Converting a negative
to a positive simply involves multiplying it by
-1 .
Note that the 0 value is neither positive nor
negative, meaning that a 0 can't convert an
adjacent negative to a positive.
A single pass through the matrix involves
converting all the negative integers that can
be converted at a particular point in time.


For example, consider the following input
matrix:
[
 [0, -2, -1],
 [-5, 2, 0],
 [-6, -2, 0],
]

After a rst pass, only 2 values can be
converted to positives:
[
 [0, 2, -1],
 [5, 2, 0],
 [-6, 2, 0],
]

After a second pass, the remaining negative
values can all be converted to positives:
[
 [0, 2, 1],
 [5, 2, 0],
 [6, 2, 0],
]

Note that the input matrix will always
contain at least one element. If the negative
integers in the input matrix can't all be
converted to positives, regardless of how
many passes are run, your function should
return -1 .

Sample Input
matrix = [
 [0, -1, -3, 2, 0],
 [1, -2, -5, -1, -3],
 [3, 0, 0, -4, -1],
]

Sample Output
3


"""
matrix = [
 [0, -1, -3, 2, 0],
 [1, -2, -5, -1, -3],
 [3, 0, 0, -4, -1],
]

# O(n * m) time, O(n * m) space, n,m是matrix的长和宽
# 方法一，用一个队列保存当前所有的正数，用第二个队列保存下一次循环要用的正数，就是这次循环负数变换过去的正数，每过一次循环就改变一下两个队列
# 方法二，下面的解法，只用一个队列，每次记录目前队列长度来循环，用过的正数pop掉，这个循环完毕之后，记录passes+1，在走下一个循环，这样新添加的由负数变成的正数不会被循环进去，

def minimumPassesOfMatrix(matrix):
	passes = convertNegatives(matrix)
	# 全部转换完成之后，还有负数，则说明没办法转换，返回-1
	if not containsNegative(matrix):
		return passes -1
	else:
		return -1

def convertNegatives(matrix):
	# 第一遍先把所有正数放进队列
	queue = getAllPositivePositions(matrix)
	passes = 0
	while len(queue) > 0:
		# 第一遍循环的数值
		currentSize = len(queue)
		while currentSize > 0:
			# 正常情况下python pop元素是O(n) time，实际上如果用queue的话，应该是O(1)time，这里是模拟queue
			# 取出一个正数，找到它的四个邻居坐标放进adjacentPositions
			currentRow,currentCol = queue.pop(0)
			adjacentPositions = getAllAdjacentPositions(currentRow,currentCol,matrix)
			for position in adjacentPositions:
				row,col = position
				value = matrix[row][col]
				# 如果邻居数值小于零 则把负数变为正数，同时把这个正数坐标添加到队列里，下一轮在循环他们
				if value < 0:
					matrix[row][col] *= -1
					queue.append([row,col])
			# while循环控制变量，只循环到当前这一轮添加的正数
			currentSize -= 1
		# 走过一遍，次数+1
		passes += 1
	return passes

def getAllPositivePositions(matrix):
	positivePositions = []
	# 永远记住 matrix横竖遍历，先横再竖，先row再col
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if  matrix[row][col] > 0:
				# 这里是添加一对数值，作为数组添加进去，取出来的时候赋值比较方便
				positivePositions.append([row,col])
	return positivePositions

def getAllAdjacentPositions(row,col,matrix):
	adjacentPositions = []
	
	if row > 0:
		adjacentPositions.append([row-1,col]) # 第一行除外，不加，其他的添加上面的相邻坐标
	if row < (len(matrix)-1):
		adjacentPositions.append([row+1,col]) # 最后一行除外，其他的添加下面的
	if col > 0:
		adjacentPositions.append([row,col-1]) # 第一列除外，其他添加左边的
	if col < len(matrix[row])-1:
		adjacentPositions.append([row,col+1]) # 最后一列除外，其他添加右边的
	
	return adjacentPositions


def containsNegative(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			if matrix[row][col] < 0:
				return True
	return False
