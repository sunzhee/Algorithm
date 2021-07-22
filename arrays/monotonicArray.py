"""
Monotonic Array
Write a function that takes in an array of integers and returns a
boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right,
are entirely non-increasing or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively
decreasing; they simply don't increase. Similarly, non-decreasing
elements aren't necessarily exclusively increasing; they simply
don't decrease.
Note that empty arrays and arrays of one element are monotonic.


Sample Input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output
true



"""


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

#O(n) time, O(1) space, n is array length
def isMonotonic(array):

	#we dont know the monotonic's direction, 
	#so first set both direction are True
	isNonIncresing = True
	isNonDecresing = True
	for i in range(1,len(array)):
		#if current number is greater than previous number,
		#then, this is decreasing, so not a increasing and increase set to False
		if (array[i] > array[i-1]):
			isNonDecresing = False
		#if current number is lesser than previous number,
		#then this is increasing, so not a decreasing and decrease set to False
		if (array[i] < array[i-1]):
			isNonIncresing = False
	return isNonIncresing or isNonDecresing


print("input array:",array)
print("output:",isMonotonic(array))


