"""
Longest Peak
Write a function that takes in an array of integers and returns the
length of the longest peak in the array.
A peak is dened as adjacent integers in the array that are
strictly increasing until they reach a tip (the highest value in the
peak), at which point they become strictly decreasing. At least
three integers are required to form a peak.
For example, the integers 1, 4, 10, 2 form a peak, but the
integers 4, 0, 10 don't and neither do the integers
1, 2, 2, 0 . Similarly, the integers 1, 2, 3 don't form a
peak because there aren't any strictly decreasing integers after
the 3 .


Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output
6 // 0, 10, 6, 5, -1, -3

"""




array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]



def longestPeak(array):
	"""
	peak check is from the second element to the second last element.
	no need to check the first and last element, definitely not peak

	because right and left id are pointing outside the peak edge, 
	so peak length is (rightId - leftId - 1)
	for instance: 4,0,10,6,5,-1,-3,2,
	leftId point to 4, rightId point to 2
	pleak length is 0 to -3 so it is 6
	"""
	longestPeakLength = 0

	for currentId in range(1,len(array) - 1):
		if array[currentId] > array[currentId - 1] and array[currentId] > array[currentId + 1]:
			leftId = currentId - 2
			rightId = currentId + 2
			while leftId >= 0 and array[leftId] < array[leftId + 1]:
				leftId -= 1
			while rightId < len(array) and array[rightId] < array[rightId - 1]:
				rightId += 1

			currentPeakLength = rightId - leftId - 1
			longestPeakLength = max(currentPeakLength,longestPeakLength)
			currentId = rightId
		else:
			currentId += 1
	return longestPeakLength



print("input:",array)
print("output:",longestPeak(array))

print(longestPeak.__doc__)