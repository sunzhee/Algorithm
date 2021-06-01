"""
Subarray Sort

Write a function that takes in an array of at
least two integers and that returns an array of
the starting and ending indices of the smallest
subarray in the input array that needs to be
sorted in place in order for the entire input
array to be sorted (in ascending order).
If the input array is already sorted, the
function should return [-1, -1] .


Sample Input
array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Sample Output
[3, 9]

"""

# O(n) time, O(1) space
# 先判断每一个位置的数值是否比前面小，比后面大，是则说明这个位置是乱序
# 比较出来最大乱序值和最小乱序值，找到左右边界，中间就是这个subArray
def subarraySort(array):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	for i in range(len(array)):
		number = array[i]
		if isOutOfOrder(i,number,array):
			minOutOfOrder = min(minOutOfOrder,number)
			maxOutOfOrder = max(maxOutOfOrder,number)
	# 如果没变，说明array都是顺序的，返回[-1,-1]，只要判断minOutOfOrder一个就可以了，或者判断max
	if minOutOfOrder == float("inf"):
		return [-1,-1]
	# 从左往右检查out of order最小值应该在哪个位置，这里就是subArray的起始
	# 从右往左检查out of order最大值应该在哪个位置，这里就是subArray的结束
	subArrayLeftIndex = 0
	subArrayRightIndex = len(array) - 1
	while minOutOfOrder >= array[subArrayLeftIndex]:
		subArrayLeftIndex += 1
	while maxOutOfOrder <= array[subArrayRightIndex]:
		subArrayRightIndex -= 1
		
	return [subArrayLeftIndex,subArrayRightIndex]
	
def isOutOfOrder(i,number,array):
	# 判断第一个和最后一个数字时的 edge case，值判断一边
	if i == 0:
		return number > array[i+1]
	if i == len(array)-1:
		return number < array[i-1]
	# 正常情况要判断i的两边
	return number > array[i+1] or number < array[i-1]
	