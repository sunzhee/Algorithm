# 2D matrix
# a 5 x 6 matrix
array0 =[
	[1,2,3,4,5],
	[6,7,8,9,10],
	[11,12,13,14,15],
	[16,17,18,19,20],
	[21,22,23,24,25],
	[26,27,28,29,30]
]

def traverse2DMatrix(array):

	print("array width:", len(array[0]))
	print("array width index range: 0 to", len(array[0]) - 1)
	print("array height:",len(array))
	print("array height index range: 0 to",len(array) - 1)

	print("first column:")
	for idx in range(len(array)):
		print(array[idx][0])

	print("last column")
	for idx in range(len(array)):
		print(array[idx][len(array[0])-1])

	return None

#print(traverse2DMatrix(array0))

#########################

array1 =[
	[0,0,0,1,1],
	[0,1,0,0,1],
	[1,1,1,1,0],
	[1,0,1,0,0],
	[0,0,0,1,1],
	[0,0,1,1,1]
]

def findIslandInMatrix(array):
	islands = []
	maxRow = len(array)
	maxColumn = len(array[0])
	#checkQueue = [[0,0]]
	for row in range(0,maxRow):
		for column in range(0,maxColumn):
		#row,col = checkQueue.pop()
			print(row,column)
			if array[row][column] != 1:
				continue
			#callDFS(array,islands,row,column)
			array[row][column] = 2

	return array

def callDFS(array,islands,startRow,startColumn):
	if array[startRow][startColumn] == 0:
		return
	if array[startRow][startColumn] == 1:
		islands.append([startRow,startColumn])
		print(islands)
		if startRow-1 >= 0:
			callDFS(array,islands,startRow-1,startColumn)
		if startRow+1 < len(array[0]):
			callDFS(array,islands,startRow+1,startColumn)
		if startColumn-1 >= 0:
			callDFS(array,islands,startRow,startColumn-1)
		if startColumn+1 < len(array):
			callDFS(array,islands,startRow,startColumn+1)
	return islands


array1 = findIslandInMatrix(array1)

for rows in range(len(array1)):
	print(array1[rows])
























