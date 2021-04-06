"""
Spiral Traverse
Write a function that takes in an n x m two-dimensional array
(that can be square-shaped when n == m) and returns a onedimensional array of all the array's elements in spiral order.
Spiral order starts at the top left corner of the two-dimensional
array, goes to the right, and proceeds in a spiral pattern all the
way until every element has been visited.



Sample Input
array = [
 [1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7],
]



Sample Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 

"""


array = [
 [1, 2, 3, 4],
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7],
]


def spiralTraverse(array):
	result = []
	startRow = 0
	endRow = len(array) - 1
	startCol = 0
	endCol = len(array[0]) -1
	while startRow <= endRow and startCol<=endCol:
		for cols in range(startCol,endCol + 1):
			result.append(array[startRow][cols])
			
		for rows in range(startRow + 1,endRow + 1):
			result.append(array[rows][endCol])
		
		for col in reversed(range(startCol,endCol)):
			if startRow == endRow:
				break
			result.append(array[endRow][col])
			
		for row in reversed(range(startRow + 1,endRow)):
			if startCol == endCol:
				break
			result.append(array[row][startCol])
		
		startRow +=1
		endRow -=1
		startCol +=1
		endCol -=1
	return result

print("input array:")
for i in range(0,len(array)):
	print(array[i])

print("Output:",spiralTraverse(array))