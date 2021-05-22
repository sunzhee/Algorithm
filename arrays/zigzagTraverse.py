"""
Zigzag Traverse

Write a function that takes in an n x m twodimensional array (that can be square-shaped
when n == m) and returns a one-dimensional
array of all the array's elements in zigzag
order.
Zigzag order starts at the top left corner of
the two-dimensional array, goes down by one
element, and proceeds in a zigzag pattern all
the way to the bottom right corner.


Sample Input
array = [
 [1, 3, 4, 10],
 [2, 5, 9, 11],
 [6, 8, 12, 15],
 [7, 13, 14, 16],
]


Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16]

"""
# O(n) time, O(n) space
# 关键是箭头指向，触左边界和下边界改为向上，触上边界和右边界改为向下，附加各种条件判断
def zigzagTraverse(array):
	maxRow = len(array) - 1 # height
	maxCol = len(array[0]) - 1 # width
	result = []
	row,col = 0,0
	goingDown = True
	
	while isOutOfBounds(row,col,maxRow,maxCol):
		result.append(array[row][col])
		if goingDown:
			if row == maxRow or col == 0:#最左边，或者最下边
				goingDown = False
				# 这里if顺序不能反过来，要优先判断最大值row == maxRow
				#     如果先判断col == 0那么row += 1就会出界，
				if row == maxRow: #最下面那条边
					col += 1
				else: #最左边那条边
					row += 1
			else: #正常情况，在方块中间向上走，继续左下
				row += 1
				col -= 1
		else: # 往上走
			if row == 0 or col == maxCol: #最上边，或者最右边
				goingDown = True
				# 同上，这里if顺序不能反过来，要优先判断最大值col == maxCol
				#     如果先判断row == 0那么col += 1就会出界，
				if col == maxCol: #最右边
					row += 1
				else: #最上边
					col += 1
			else: # 正常情况，在方块中间向上走，继续右上
				row -= 1
				col += 1
	return result
					
def isOutOfBounds(row,col,maxRow,maxCol):
	if row > maxRow or col > maxCol or row < 0 or col < 0:
		return False
	return True
	
