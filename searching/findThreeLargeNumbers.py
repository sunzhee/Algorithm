"""
Find Three Largest Numbers
Write a function that takes in an array of at least three integers
and, without sorting the input array, returns a sorted array of the
three largest integers in the input array.
The function should return duplicate integers if necessary; for
example, it should return [10, 10, 12] for an input array of
[10, 5, 9, 10, 12] .




Sample Input
[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

Sample Output
[18, 141, 541]




"""




#O(n) time, O(1) space
def findThreeLargestNumbers(array):
	largestNumber = [None,None,None]
	for num in array:
		if  largestNumber[2] is None or num > largestNumber[2]:
			largestNumber[0] = largestNumber[1]
			largestNumber[1] = largestNumber[2]
			largestNumber[2] = num
			
		elif largestNumber[1] is None or num >largestNumber[1]:
			largestNumber[0] = largestNumber[1]
			largestNumber[1] = num
		
		elif largestNumber[0] is None or num > largestNumber[0]:
			largestNumber[0] = num
			
	return largestNumber
			