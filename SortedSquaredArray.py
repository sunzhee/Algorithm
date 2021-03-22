'''
Sorted Squared Array
Write a function that takes in a non-empty array of integers that
are sorted in ascending order and returns a new array of the
same length with the squares of the original integers also sorted
in ascending order.

While the integers in the input array are sorted in
increasing order, their squares won't necessarily be as well,
because of the possible presence of negative numbers.


Sample Input
array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
[1, 4, 9, 25, 36, 64, 81]

'''
#input sample
array = [1, 2, 3, 5, 6, 8, 9]
array = [-10,-5,0,5,10]



def sortedSquaredArray1(array):
	result = []
	for i in range(len(array)):
		result.append(array[i]*array[i])
	result.sort()
	return result


def sortedSquaredArray2(array):
	#init a result array same length with input array
	result = [0 for _ in array]
	leftPointer = 0
	rightPointer = len(array) - 1

	#i is the right most result array index
	#so this for loop is begin with len(array)-1(the last number in array) decrease to 0(the first number in array) by step -1
	#this for can write in simple mode like this:
	#for i in reversed(range(len(array))):
	for i in range(len(array) -1 ,-1 ,-1):
		leftValue = array[leftPointer]
		rightValue = array[rightPointer]
		if abs(leftValue) > abs(rightValue):
			result[i] = leftValue * leftValue
			leftPointer = leftPointer + 1
		else:
			result[i] = rightValue * rightValue
			rightPointer = rightPointer - 1
	return result

print ("input:",array)
print ("output:",sortedSquaredArray1(array))