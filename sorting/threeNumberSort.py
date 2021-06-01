"""
Three Number Sort

You're given an array of integers and another
array of three distinct integers. The rst array
is guaranteed to only contain integers that
are in the second array, and the second array
represents a desired order for the integers in
the rst array. For example, a second array of
[x, y, z] represents a desired order of
[x, x, ..., x, y, y, ..., y, z, z, ...
in the rst array.
Write a function that sorts the rst array
according to the desired order in the second
array.
The function should perform this in place (i.e.,
it should mutate the input array), and it
shouldn't use any auxiliary space (i.e., it
should run with constant space: O(1)
space).
Note that the desired order won't necessarily
be ascending or descending and that the rst
array won't necessarily contain all three
integers found in the second array—it might
only contain one or two.


Sample Input
array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]

Sample Output
[0, 0, 0, 1, 1, 1, -1, -1]

"""
# O(n) time, O(1) space
# loop 2 times
def threeNumberSort(array, order):
	firstValue = order[0]
	thirdValue = order[2]
	
	firstIndex = 0
	secondIndex = len(array) - 1
	for i in range(len(array)):
		if array [i] == firstValue:
			array[i],array[firstIndex] = array[firstIndex],array[i]
			firstIndex += 1
	
	for i in range(len(array)-1,-1,-1):
		if array[i] == thirdValue:
			array[i],array[secondIndex] = array[secondIndex],array[i]
			secondIndex -= 1
	return array

# O(n) time, O(1) space
# loop only 1 times
def threeNumberSort(array, order):
	firstValue = order[0]
	secondValue = order[1]
	firstIndex = 0
	secondIndex = 0
	thirdIndex = len(array) - 1
	
	while secondIndex <= thirdIndex:
		currentValue = array[secondIndex]
		
		if currentValue == firstValue:
			array[secondIndex],array[firstIndex] = array[firstIndex],array[secondIndex]
			firstIndex += 1
			secondIndex += 1
		elif currentValue == secondValue:
			# array[i],array[secondIndex] = array[secondIndex],array[i]
			secondIndex += 1
		else:
			array[secondIndex],array[thirdIndex] = array[thirdIndex],array[secondIndex]
			thirdIndex -= 1
	return array
