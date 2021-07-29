"""

Smallest Difference
Write a function that takes in two non-empty arrays of integers,
nds the pair of numbers (one from each array) whose absolute
dierence is closest to zero, and returns an array containing
these two numbers, with the number from the rst array in the
rst position.
Note that the absolute dierence of two integers is the distance
between them on the real number line. For example, the
absolute dierence of -5 and 5 is 10, and the absolute dierence
of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with
the smallest dierence.


Sample Input
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
Sample Output
[28, 26]

"""

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

#have both array sorted
#use a pointer at each array beginning, compair the difference
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	index1 = 0
	index2 = 0
	currentDiff = float("inf")
	smallestDiff = float("inf")
	resultArray = []
	
	while index1 < len(arrayOne) and index2 < len(arrayTwo):
		currentDiff = abs(arrayOne[index1] - arrayTwo[index2])
		if currentDiff < smallestDiff:
			smallestDiff = currentDiff
			resultArray = [arrayOne[index1],arrayTwo[index2]]
			# 这里只能先记录下来返回结果resultArray，然后再最后返回，如果不这么做，下面的判断还会再把下标+1，直接导致数组下标出界
			# 如果要单独列出来if判断下表是否到最后一个，这样做还是会导致返回值下标出界，这个if判断没法使用，会使一个数组到头，但是另一个数组没有走到比前面数组最近的最后一个
			#if indexOne+1 >= len(arrayOne) and indexTwo+1 >=len(arrayTwo):
			#	break
		if arrayOne[index1] < arrayTwo[index2]:
			index1 +=1
		elif arrayOne[index1] > arrayTwo[index2]:
			index2 +=1
		else:
			return [arrayOne[index1],arrayTwo[index2]]
	return resultArray

print (smallestDifference(arrayTwo,arrayOne))
