"""
Sunset Views

Given an array of buildings and a direction
that all of the buildings face, return an array
of the indices of the buildings that can see
the sunset.
A building can see the sunset if it's strictly
taller than all of the buildings that come after
it in the direction that it faces.
The input array named buildings
contains positive, non-zero integers
representing the heights of the buildings. A
building at index i thus has a height
denoted by buildings[i] . All of the
buildings face the same direction, and this
direction is either east or west, denoted by
the input string named direction , which
will always be equal to either "EAST" or
"WEST" . In relation to the input array, you
can interpret these directions as right for
east and left for west.
Important note: the indices in the ouput
array should be sorted in ascending order

Sample Input #1
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"

Sample Output #1
[1, 3, 6, 7]
// Below is a visual representation of the sample input.
//    _
//   | |_ _
//  _| | | |_   _
// | | | | | | | |_
// | | | | | |_| | |
// |_|_|_|_|_|_|_|_|



Sample Input #2
buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"


Sample Output #2
[0, 1]
// The buildings are the same as in the first sample
// input, but their direction is reversed.



"""

# O(n) time ,O(n) space
# 数组比较
def sunsetViews(buildings, direction):
	resultBuildings = []
	
	# 同时处理两个方向，如果是west则从左到右step +1，如果是east则从右到左，step -1
	startIndex = 0 if direction == "WEST" else len(buildings) - 1
	step = 1 if direction == "WEST" else -1
	
	currentHeight = 0
	
	while startIndex >= 0 and startIndex < len(buildings):
		if buildings[startIndex] > currentHeight:
			resultBuildings.append(startIndex)	
		currentHeight = max(currentHeight,buildings[startIndex])
		# 如果是顺序，则为+1，如果是逆序则为-1
		startIndex += step	
	# 输出结果要求顺序
	if direction != "WEST":
		resultBuildings = resultBuildings[::-1]
			
	return resultBuildings

# O(n) time, O(n) space
# 用stack，一个一个比较，小的pop掉
def sunsetViews(buildings, direction):
	resultBuildings = []
	
	loopIndex = 0 if direction == "EAST" else len(buildings) - 1
	step = 1 if direction == "EAST" else -1
	
	while loopIndex >=0 and loopIndex < len(buildings):
		while len(resultBuildings) > 0 and buildings[resultBuildings[-1]] <= buildings[loopIndex]:
			resultBuildings.pop()
		resultBuildings.append(loopIndex)
		loopIndex += step
	if direction != "EAST":
		resultBuildings = resultBuildings[::-1]
		
	return resultBuildings
