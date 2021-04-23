"""
Number Of Ways To Traverse Graph

You're given two positive integers representing the width and
height of a grid-shaped, rectangular graph. Write a function that
returns the number of ways to reach the bottom right corner of
the graph when starting at the top left corner. Each move you
take must either go down or right. In other words, you can never
move up or left in the graph.
For example, given the graph illustrated below, with
width = 2 and height = 3 , there are three ways to reach
the bottom right corner when starting at the top left corner:
 _ _
|_|_|
|_|_|
|_|_|

1. Down, Down, Right
2. Right, Down, Down
3. Down, Right, Down

Note: you may assume that width * height >= 2 . In other
words, the graph will never be a 1x1 grid.

Sample Input
width = 4
height = 3

Sample Output
10

"""

width = 4
height = 3


# O(2^(n+m)) Time | O(n+m) space
# recursive solution, not time optimized, but simple
def numberOfWaysToTraverseGraph1(width, height):
	# hit the base case, all up and left border is 1
	if width == 1 or height == 1:
		return 1
	return numberOfWaysToTraverseGraph(width - 1,height) + numberOfWaysToTraverseGraph(width,height - 1)


#O(n*m) time | O(n*m) space
#dynamic programming solution
def numberOfWaysToTraverseGraph(width, height):
	ways = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

	for widthIndex in range(1,width + 1):
		for heightIndex in range(1,height + 1):
			if widthIndex == 1 or heightIndex == 1:
				ways[heightIndex][widthIndex] = 1
			else:
				leftValue = ways[heightIndex][widthIndex - 1]
				upValue = ways[heightIndex - 1][widthIndex]
				ways[heightIndex][widthIndex] = leftValue + upValue
	return ways[height][width]


print("output:",numberOfWaysToTraverseGraph(width,height))