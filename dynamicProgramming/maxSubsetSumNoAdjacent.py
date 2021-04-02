"""
Max Subset Sum No Adjacent
Write a function that takes in an array of positive integers and
returns the maximum sum of non-adjacent elements in the array.
If the input array is empty, the function should return 0 .


Sample Input
array = [75, 105, 120, 75, 90, 135]

Sample Output
330 // 75 + 120 + 135

"""






#O(n) time, O(n) space

array = [75, 105, 120, 75, 90, 135]

def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	elif len(array) == 1:
		return array[0]
	
	#define maxSum same length and same each value as given array
	maxSum = array[:]
	#calculate the second value maxSum[1] of our maxSum array
	#the first value is equal to array[i]
	#then we can use for loop to go forward
	maxSum[1] = max(array[0],array[1])
	
	for i in range(2,len(array)):
		maxSum[i] = max(maxSum[i-1],maxSum[i-2] + array[i])
	
	return maxSum[-1]


print("input:",array)
print("output:",maxSubsetSumNoAdjacent(array))
	
	

