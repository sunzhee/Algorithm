"""
Remove Islands

You're given a two-dimensional array (a matrix) of
potentially unequal height and width containing only 0 s
and 1 s. The matrix represents a two-toned image,
where each 1 represents black and each 0 represents
white. An island is dened as any number of 1 s that are
horizontally or vertically adjacent (but not diagonally
adjacent) and that don't touch the border of the image. In
other words, a group of horizontally or vertically adjacent
1 s isn't an island if any of those 1 s are in the rst row,
last row, rst column, or last column of the input matrix.
Note that an island can twist. In other words, it doesn't
have to be a straight vertical line or a straight horizontal
line; it can be L-shaped, for example.
You can think of islands as patches of black that don't
touch the border of the two-toned image.
Write a function that returns a modied version of the
input matrix, where all of the islands are removed. You
remove an island by replacing it with 0 s.
Naturally, you're allowed to mutate the input matrix.

Sample Input
matrix =
[
 [1, 0, 0, 0, 0, 0],
 [0, 1, 0, 1, 1, 1],
 [0, 0, 1, 0, 1, 0],
 [1, 1, 0, 0, 1, 0],
 [1, 0, 1, 1, 0, 0],
 [1, 0, 0, 0, 0, 1]
]


Output
[
 [1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 0],
 [1, 1, 0, 0, 1, 0],
 [1, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 1]
]
// The islands that were removed can be clearly see
// [
// [ , , , , , ],
// [ ,1, , , , ],
// [ , ,1, , , ],
// [ , , , , , ],
// [ , ,1,1, , ],
// [ , , , , , ]


"""

# O(m*n) time | O(m*n) space
# m, n is matrix length and width
# 先处理四条边，定义一个标记matrix，把每一条边上的1的邻居用DFS全部标记出来，为True，这些位置不删除
# 然后处理中间部分，全部没有标记为True的都换成0
# 为了节省内存，可以不用新建标记Matrix，直接在原matrix上把非island标记为2，或者-1，然后所有位置不是2的统统改为0，所有2改为1

def removeIslands(matrix):
	booleanMatrix = [[False for col in matrix[0]] for row in matrix]
	# Find all border "1", and marked as True for not an island
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			isBorder = False
			# 1st row, 1 col, last row, last col
			# this is border
			if row == 0 or col == 0 or row == len(matrix) - 1 or col == len(matrix[row]) - 1:
				isBorder = True
			# why can not use other ways? yes, but not marked here, need marked in DFS
				# yes, can use this way, but it's better to use continue, to cover all the conditions
			#if isBorder and matrix[row][col] == 1 and booleanMatrix[row][col] == False:
				#markAllNeighborsDFS(matrix,row,col,booleanMatrix)
				
			# not border, skip current loop
			if not isBorder:
				continue
			# not 1, it is 0, so skip current loop
			if matrix[row][col] != 1:
				continue		
			# it is 1, and it is border, so mark all neighbors has 1 with True, at booleanMatrix
			markAllNeighborsDFS(matrix,row,col,booleanMatrix)
	
	for row in range(1,len(matrix) - 1):
		for col in range(1,len(matrix[row]) - 1):
			if booleanMatrix[row][col] == True:
				continue
			matrix[row][col] = 0
	return matrix
	
def markAllNeighborsDFS(matrix,startRow,startCol,booleanMatrix):
	# DFSstack is an array which each element has two attributes, row and col
	DFSstack = [(startRow,startCol)]
	while len(DFSstack) > 0:
		currentPosition = DFSstack.pop()
		currentRow,currentCol = currentPosition
		visitedOrNot = booleanMatrix[currentRow][currentCol]
		# we came here mark True, because it is 1 and it is border,not island
		#why can not use other way?
			# because continue is break the current while loop
			# in this case, if we meet visited node and without continue, 
			# it will get infinity loop at this node, never going out.
		if visitedOrNot == True:
			continue
		else:
			booleanMatrix[currentRow][currentCol] = True
		
		# next we mark all it's neighbor has 1 , as True
		# we need find all neighbor first, then append them to the DFSstack
		# and DFS will mark them one by one.
		neighbors = retriveAllNeighbor(matrix,currentRow,currentCol)
		# neighbors is an array which each element has two attributes, row and col
		# neighbors is same as DFSstack, so we can append it
		for neighbor in neighbors:
			row,col = neighbor
			# why can not use other ways?
			#if == 1 then append?
				# it is ok, we need continue to break out the current loop,
				# since it has no operation after the "if cluse", so it doesn't matter,
				# but if after "if cluse" there is aother operations,it may got infinity loop
				# the best safe way is write both conditions, one is operation and one is continue.
			if matrix[row][col] != 1:
				continue
			else:
				DFSstack.append(neighbor)
			
			#if matrix[row][col] == 1:
			#	DFSstack.append(neighbor)
		
def retriveAllNeighbor(matrix,currentRow,currentCol):
	neighbors = []
	# UP neighbor
	# if row - 1 is not out of top bound, we have UP side neighbor, we add it to neighbors
	if currentRow - 1 >= 0:
		neighbors.append((currentRow - 1,currentCol))
	# DOWN neighbor, row + 1 not out of bottom bound, add it
	if currentRow + 1 < len(matrix):
		neighbors.append((currentRow + 1,currentCol))
	# LEFT neighbor,
	if currentCol -1 >= 0:
		neighbors.append((currentRow,currentCol - 1))
	# RIGHT neighbor
	if currentCol + 1 < len(matrix[currentRow]):
		neighbors.append((currentRow,currentCol + 1))
	
	# we return three neighbors at border, two neighbors at corner
	print(neighbors)
	return neighbors