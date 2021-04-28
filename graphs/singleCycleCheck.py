"""
Single Cycle Check
You're given an array of integers where each
integer represents a jump of its value in the
array. For instance, the integer 2 represents
a jump of two indices forward in the array;
the integer -3 represents a jump of three
indices backward in the array.
If a jump spills past the array's bounds, it
wraps over to the other side. For instance, a
jump of -1 at index 0 brings us to the last
index in the array. Similarly, a jump of 1 at
the last index in the array brings us to index
0 .
Write a function that returns a boolean
representing whether the jumps in the array
form a single cycle. A single cycle occurs if,
starting at any index in the array and
following the jumps, every element in the
array is visited exactly once before landing
back on the starting index.


Sample Input
array = [2, 3, 1, -4, -4, 2]


Sample Output
true

"""

#O(n) time | O(1) space
#loop thru for len(array) times, if we return the start index, return true, else return false.
def hasSingleCycle(array):
	visitedNumber = 0
	startIndex = 0
	while visitedNumber < len(array):
		#this if can handle the start value is 0, it never move, 
		#after loop len(array) times,it still at start point, should not be True
		if visitedNumber != 0 and visitedNumber < len(array) and startIndex == 0:
			return False
		startIndex = getIndex(startIndex,array)
		visitedNumber += 1
	
	if visitedNumber == len(array) and startIndex == 0:
		return True
	else:
		return False

#  index jump function, two edge cases: out of right bound, out of left bound
# % handle the right outbound
# % + len(array) handle the left outbound
def getIndex(index,array):
	returnIndex = (index + array[index]) % len(array)
	if returnIndex < 0:
		returnIndex = returnIndex + len(array)
	return returnIndex