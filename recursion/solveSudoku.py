"""
Solve Sudoku

You're given a two-dimensional array that
represents a 9x9 partially lled Sudoku
board. Write a function that returns the
solved Sudoku board.
Sudoku is a famous number-placement
puzzle in which you need to ll a 9x9 grid
with integers in the range of 1-9 . Each 9x9
Sudoku board is split into 9 3x3 subgrids, as
seen in the illustration below, and starts out
partially filled.

- - 3 | - 2 - | 6 - -
9 - - | 3 - 5 | - - 1
- - 1 | 8 - 6 | 4 - -
- - - - - - - - - - -
- - 8 | 1 - 2 | 9 - -
7 - - | - - - | - - 8
- - 6 | 7 - 8 | 2 - -
- - - - - - - - - - -
- - 2 | 6 - 9 | 5 - -
8 - - | 2 - 3 | - - 9
- - 5 | - 1 - | 3 - -

The objective is to ll the grid such that each
row, column, and 3x3 subgrid contains the
numbers 1-9 exactly once. In other words,
no row may contain the same digit more
than once, no column may contain the same
digit more than once, and none of the 9 3x3
subgrids may contain the same digit more
than once.

Your input for this problem will always be a
partially lled 9x9 two-dimensional array
that represents a solvable Sudoku puzzle.
Every element in the array will be an integer
in the range of 0-9 , where a 0 represents
an empty square that must be lled by your
algorithm.
Note that you may modify the input array
and that there will always be exactly one
solution to each input Sudoku board.


Sample Input
board =
[
 [7, 8, 0, 4, 0, 0, 1, 2, 0],
 [6, 0, 0, 0, 7, 5, 0, 0, 9],
 [0, 0, 0, 6, 0, 1, 0, 7, 8],
 [0, 0, 7, 0, 4, 0, 2, 6, 0],
 [0, 0, 1, 0, 5, 0, 9, 3, 0],
 [9, 0, 4, 0, 6, 0, 0, 0, 5],
 [0, 7, 0, 3, 0, 0, 0, 1, 2],
 [1, 2, 0, 0, 0, 7, 4, 0, 0],
 [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

Sample Output

[
 [7, 8, 5, 4, 3, 9, 1, 2, 6],
 [6, 1, 2, 8, 7, 5, 3, 4, 9],
 [4, 9, 3, 6, 2, 1, 5, 7, 8],
 [8, 5, 7, 9, 4, 3, 2, 6, 1],
 [2, 6, 1, 7, 5, 8, 9, 3, 4],
 [9, 3, 4, 1, 6, 2, 7, 8, 5],
 [5, 7, 8, 3, 9, 4, 6, 1, 2],
 [1, 2, 6, 5, 8, 7, 4, 9, 3],
 [3, 4, 9, 2, 1, 6, 8, 5, 7],
]

"""

{
  "board": [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]
}

# O(1)time , O(1) space
# 因为是9x9的格子，复杂度是恒定常数，所以为O(1)，但是实际上要运算很长时间
def solveSudoku(board):
	solvePartialSudoku(0,0,board)
	return board

def solvePartialSudoku(row,col,board):
	currentRow = row
	currentCol = col
	
	# col走到头之后，折返，row + 1，col归0
	if currentCol == len(board[currentRow]):
		currentRow += 1
		currentCol = 0
		if currentRow == len(board):
			return True # 到这里是全部走完了
	
	if board[currentRow][currentCol] == 0:
		return tryDigitsAtPosition(currentRow,currentCol,board)
	
	return solvePartialSudoku(currentRow,currentCol + 1,board)

def tryDigitsAtPosition(row,col,board):
	for digit in range(1,10):
		if isValidAtPosition(digit,row,col,board):
			board[row][col] = digit
			if solvePartialSudoku(row,col + 1,board):
				return True
	# 如果不成立，退回去以后，要把这一位置重新归0
	board[row][col] = 0
	return False

	
def isValidAtPosition(value,row,col,board):
	rowIsValid = value not in board[row]
	columnIsValid = value not in map(lambda r:r[col],board)
		# lambda是表示参数,map表示一个一个处理
	
	if not rowIsValid or not columnIsValid:
		return False
	
	# check subgrid valid
	subgridRowStart = (row // 3) * 3
	subgridColStart = (col // 3) * 3
	for rowIdx in range(3):
		for colIdx in range(3):
			rowToCheck = subgridRowStart + rowIdx
			colToCheck = subgridColStart + colIdx
			existingValue = board[rowToCheck][colToCheck]
			if existingValue == value:
				return False
		
	return True
