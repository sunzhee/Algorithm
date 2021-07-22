"""
Largest Rectangle Under Skyline


Write a function that takes in an array of positive integers
representing the heights of adjacent buildings and returns the area of
the largest rectangle that can be created by any number of adjacent
buildings, including just one building. Note that all buildings have the
same width of 1 unit.
For example, given buildings = [2, 1, 2] , the area of the
largest rectangle that can be created is 3 , using all three buildings.
Since the minimum height of the three buildings is 1 , you can
create a rectangle that has a height of 1 and a width of 3 (the
number of buildings). You could also create rectangles of area 2 by
using only the rst building or the last building, but these clearly
wouldn't be the largest rectangles. Similarly, you could create
rectangles of area 2 by using the rst and second building or the
second and third building.
To clarify, the width of a created rectangle is the number of buildings
used to create the rectangle, and its height is the height of the
smallest building used to create it.
Note that if no rectangles can be created, your function should return
0 .


Sample Input
buildings = [1, 3, 3, 2, 4, 1, 5, 3, 2]

Sample Output
9

// Below is a visual representation of the sample input.
//              _
//          _  | |
//    _ _  | | | |_
//   | | |_| | | | |_
//  _| | | | |_| | | |
// |_|_|_|_|_|_|_|_|_|

"""

# O(n ** 2) time , O(1) space
# 挨个循环计算，每个循环内，分别向左右两边延申
# 只要左边或者右边的比当前值大于等于就继续扩展，直到遇到小于停止，计算左右边界差，乘以当前高度得出最大面积
def largestRectangleUnderSkyline(buildings):
	maxArea = 0
	for pillarIndex in range(len(buildings)):
		currentHeight = buildings[pillarIndex]
		
		leftPointer = pillarIndex
		while leftPointer > 0 and buildings[leftPointer - 1] >= currentHeight:
			leftPointer -= 1
		rightPointer = pillarIndex
		while rightPointer < len(buildings) - 1  and buildings[rightPointer + 1] >= currentHeight:
			rightPointer += 1
		
		currentBuildingArea = (rightPointer - leftPointer + 1) * currentHeight
		maxArea = max(maxArea,currentBuildingArea)
		
	return maxArea
