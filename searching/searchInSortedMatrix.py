"""
Search In Sorted Matrix
You're given a two-dimensional array (a
matrix) of distinct integers and a target
integer. Each row in the matrix is sorted, and
each column is also sorted; the matrix doesn't
necessarily have the same height and width.
Write a function that returns an array of the
row and column indices of the target integer
if it's contained in the matrix, otherwise
[-1, -1] .


Sample Input
matrix = [
 [1, 4, 7, 12, 15, 1000],
 [2, 5, 19, 31, 32, 1001],
 [3, 8, 24, 33, 35, 1002],
 [40, 41, 42, 44, 45, 1003],
 [99, 100, 103, 106, 128, 1004],
]
target = 44


Sample Output
[3, 3]


"""

def searchInSortedMatrix(matrix, target):
	row = 0
	col = len(matrix[0]) - 1
	# 从matrix右上角开始往左，往下搜索遍历，直到左下角
	while row < len(matrix) and col >=0:
		# 说明target在这个col的左边，所以col-1往左走
		if matrix[row][col] > target:
			col -= 1
		# 说明target在这个row的下面，所以row+1往下走
		elif matrix[row][col] < target:
			row +=1
		# 等于target，返回
		else:
			return [row,col]
	# 出while loop，遍历完每找到
	return [-1,-1]
			
