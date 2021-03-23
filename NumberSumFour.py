"""
Four Number Sum
Write a function that takes in a non-empty array of distinct
integers and an integer representing a target sum. The function
should nd all quadruplets in the array that sum up to the target
sum and return a two-dimensional array of all these quadruplets
in no particular order.
If no four numbers sum up to the target sum, the function
should return an empty array.

Sample Input
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

Sample Output
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets

"""


#input
array=[5,-5,-2,2,3,-3]
targetSum = 0


def fourNumberSum(array, targetSum):
	leftSideSum = {}
	result = []
	for i in range (1,len(array) - 1):
		for j in range (i + 1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if difference in leftSideSum:
				for pair in leftSideSum[difference]:
					result.append(pair + [array[i],array[j]])
					#-------------^^^^---------it will effected the leftSideSum below
		for k in range (0,i):
			currentSum = array[i] + array[k]
			if currentSum not in leftSideSum:
				leftSideSum[currentSum] = [[array[k],array[i]]]
				#-------------------------^^----------------^^^ becareful of this []
				#because this is the first line of dealing with leftSideSum, so if this 
				#line is not correct, the result array above CAN NOT add pair to array[i], because it's not a 2-d array
			else:
				leftSideSum[currentSum].append([array[k],array[i]])
	return result
		


print("input array:")
print(array)
print("input targetSum:",targetSum)
print("-------")
print("output:")
print (fourNumberSum(array,targetSum))