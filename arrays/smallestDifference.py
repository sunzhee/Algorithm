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
		if arrayOne[index1] < arrayTwo[index2]:
			index1 +=1
		elif arrayOne[index1] > arrayTwo[index2]:
			index2 +=1
		else:
			return [arrayOne[index1],arrayTwo[index2]]
	return resultArray

print (smallestDifference(arrayTwo,arrayOne))
