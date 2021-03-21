'''
Three Number Sum
Write a function that takes in a non-empty array of distinct
integers and an integer representing a target sum. The function
should nd all triplets in the array that sum up to the target sum
and return a two-dimensional array of all these triplets. The
numbers in each triplet should be ordered in ascending order,
and the triplets themselves should be ordered in ascending
order with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function
should return an empty array.


Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


'''




#T=O(N^2) S=O(N)
#sort array, one for loop and while loop with two pointer
def threeNumberSum(array, targetSum):
	array.sort()
	result = []
	# len(array) - 2 , because we need two numbers for left and right pointer
	for i in range(0,len(array)-2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				result.append([array[i],array[left],array[right]])
				#we found the triple combination,
				#append it to result and move left and right pointer at same time.
				left = left + 1
				right = right - 1
			if currentSum > targetSum:
				#currentSum is bigger then target, so we need decrease the sum, move right pointer 1 step left
				right = right - 1
			if currentSum < targetSum:
				#currentSum is less then target, we need increase the sum, move left pointer 1 step right
				left = left +1
	return result