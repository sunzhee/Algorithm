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
			print(maxRow,maxColumn,":",row,column)
			retirveNeighborsDFS(array,islands,row,column)
	return islands

def retirveNeighborsDFS(array,islands,startRow,startColumn):
	neighborsQueue = [(startRow,startColumn)]
	while len(neighborsQueue) > 0:
		row,column = neighborsQueue.pop()
		#print(row,column)

		if startRow-1 >= 0 and array[startRow-1][startColumn] == 1:
			neighborsQueue.append((startRow-1,startColumn))
		if startRow+1 < len(array) and array[startRow+1][startColumn] == 1:
			neighborsQueue.append((startRow+1,startColumn))
		if startColumn-1 >=0 and array[startRow][startColumn-1] == 1:
			neighborsQueue.append((startRow,startColumn-1))
		if startColumn+1 < len(array[0]) and array[startRow][startColumn+1] == 1:
			neighborsQueue.append((startRow,startColumn+1))



	

	return islands


print(findIslandInMatrix(array1))
























