'''
River Sizes
You're given a two-dimensional array (a
matrix) of potentially unequal height and
width containing only 0 s and 1 s. Each 0
represents land, and each 1 represents part
of a river. A river consists of any number of 1
s that are either horizontally or vertically
adjacent (but not diagonally adjacent). The
number of adjacent 1 s forming a river
determine its size.
Note that a river can twist. In other words, it
doesn't have to be a straight vertical line or a
straight horizontal line; it can be L-shaped, for
example.
Write a function that returns an array of the
sizes of all rivers represented in the input
matrix. The sizes don't need to be in any
particular order.


Sample Input
matrix = [
 [1, 0, 0, 1, 0],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0],
]


Sample Output
// 
//[1, 2, 2, 2, 5] 
// The rivers can be clearly seen
// [
// [1, , , 1,  ],
// [1, , 1, ,  ],
// [ , , 1, , 1],
// [1, , 1, , 1],
// [1, , 1, 1, ],
// ]
'''



def riverSizes(matrix):

    sizes = []
	visited = [[False for value in row] for row in matrix]
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			if visited[i][j] :
				continue
			traverseNode(i,j,matrix,visited,sizes)
	return sizes

def traverseNode(i,j,matrix,visited,sizes):
	currentRiverSize = 0
	nodesToExplore = [[i,j]]
	while len(nodesToExplore):
		currentNode = nodesToExplore.pop() #stack, DFS
		i = currentNode[0]
		j = currentNode[1]
		if visited[i][j]:
			continue #already visited skip
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue #it is a 0, skip
		currentRiverSize += 1 #it is a 1, so increase river size by 1
		unvisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited)
		for neighbor in unvisitedNeighbors:
			nodesToExplore.append(neighbor)
	if currentRiverSize > 0: #end of while loop, we have traverse the rive and have the river size
		sizes.append(currentRiverSize)
		
def getUnvisitedNeighbors(i,j,matrix,visited):
	unvisitedNeighbors = []
	
	#if it is not first row, and this nodes's upside node is not visited, then append
	if i > 0 and not visited[i-1][j]: 
		unvisitedNeighbors.append([i-1,j])
	
	#if it is not last row, and this nodes's downside node is not visited, then append
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNeighbors.append([i+1,j])
		
	#if it is not first column, and this node's left node is not visited, then append
	if j > 0 and not visited[i][j-1]:
		unvisitedNeighbors.append([i,j-1])
	
	#if it is not last column, and this node's right node is not visited, then append
	if j < len(matrix[0]) - 1 and not visited[i][j+1]:
		unvisitedNeighbors.append([i,j+1])
	return unvisitedNeighbors
	