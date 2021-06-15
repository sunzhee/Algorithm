"""
Maximum Sum Submatrix

You're given a two-dimensional array (a
matrix) of potentially unequal height and
width that's lled with integers. You're also
given a positive integer size . Write a
function that returns the maximum sum that
can be generated from a submatrix with
dimensions size * size .

For example, consider the following matrix:
[
 [2, 4],
 [5, 6],
 [-3, 2],
]

If size = 2 , then the 2x2 submatrices to
consider are:
[2, 4]
[5, 6]
------
[5, 6]
[-3, 2]
The sum of the elements in the rst
submatrix is 17 , and the sum of the
elements in the second submatrix is 10 . In
this example, your function should return
17 .

Note: size will always be at least 1 , and
the dimensions of the input matrix will
always be at least size * size .
Sample Input
matrix =
[
 [5, 3, -1, 5],
 [-7, 3, 7, 4],
 [12, 8, 0, 0],
 [1, -8, -8, 2],
]
size = 2


Sample Output
18
// [
// [., ., ., .],
// [., 3, 7, .],
// [., 8, 0, .],
// [., ., ., .],
// ]

"""

# 用size的右下角表示这个子矩阵的sums，先计算全部子矩阵sums，然后用size-1 开始往外循环
# 子矩阵的sums等于减去左面，减去上面，同时加上斜对角线，因为斜对角线被减去两次
# 碰到上边缘or左边缘，就不需要减上边缘or左边缘了
def maximumSumSubmatrix(matrix, size):
	sums = createSumMatrix(matrix)
	maxSubMatrixSum = float("-inf")
	
	for row in range(size - 1, len(matrix)):
		for col in range(size - 1,len(matrix[row])):
			total = sums[row][col]
			
			touchTopBorder = row - size < 0
			if not touchTopBorder:
				total -= sums[row - size][col]
				
			touchLeftBorder = col - size < 0
			if not touchLeftBorder:
				total -= sums[row][col - size]
			
			touchTopOrLeftBorder = touchTopBorder or touchLeftBorder
			if not touchTopOrLeftBorder:
				total += sums[row - size][col - size]
			
			maxSubMatrixSum = max(maxSubMatrixSum,total)
			
	return maxSubMatrixSum
	
	
def createSumMatrix(matrix):
	sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
	
	# 计算第一个sums[0,0]等于matrix[0,0]
	sums[0][0] = matrix[0][0]
	# 计算第一行 row，当前值加上左边一位的值
	for idx in range(1,len(matrix[0])):
		sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
	# 计算第一列 col，当前值加上上面一位的值
	for idx in range(1,len(matrix)):
		sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
	# 计算剩余的，注意范围是从1开始，跳过第一行和第一列，当前位置sums等于加上左边与上面，减去斜对角线
	for row in range(1,len(matrix)):
		for col in range(1,len(matrix[row])):
			sums[row][col] = sums[row-1][col] + sums[row][col-1] - sums[row-1][col-1] + matrix[row][col]
	return sums