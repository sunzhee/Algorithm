
"""
Two Number Sum

Write a function that takes in a non-empty array of distinct
integers and an integer representing a target sum. If any two
numbers in the input array sum up to the target sum, the
function should return them in an array, in any order. If no two
numbers sum up to the target sum, the function should return
an empty array.
Note that the target sum has to be obtained by summing two
dierent integers in the array; you can't add a single integer to
itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers
summing up to the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample Output
[-1, 11] 

"""

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


#the best way, but only for two numbers sum
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		y = targetSum -  array[i]
		if y in array and array[i] != y :
			return [array[i],y]
	return []

#the simple but not optimal way, use 2 x for loop
def twoNumbebSum2(array,targetSum):
	for i in range(0,len(array)):
		for j in range((i+1),len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
	return []


#use left and right two pointers,very important solution, can be used in three number sum and four number sum
def twoNumberSum3(array, targetSum):
	array.sort()
	left = 0
	right = len(array) -1
	while left < right:
		result = array[left] + array[right]
		if result == targetSum:
			return [array[left],array[right]]
		if result > targetSum:
			right = right - 1
		if result < targetSum:
			left = left + 1
	return []

#best solution,can be used on three or four numbe sum
#make an empty waiting set, check on number's match, if no match in the waiting set
#then return two number, if not then add the current number in wating set
#O(n) time, O(n)space
def twoNumberSum4(array, targetSum):
	tempList = {}
	for currentNumber in array:
		match = targetSum - currentNumber
		if match in tempList:
			return [currentNumber,match]
		else:
			tempList[currentNumber] = 1
	return []

print("input array:",array)
print("input targetSum:",targetSum)
print("output:",twoNumberSum3(array,targetSum))