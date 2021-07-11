"""
Index Equals Value
Write a function that takes in a sorted array of
distinct integers and returns the rst index in
the array that is equal to the value at that
index. In other words, your function should
return the minimum index where
index == array[index] .
If there is no such index, your function should
return -1 .


Sample Input
array = [-5, -3, 0, 3, 4, 5, 9]


Sample Output
3 // 3 == array[3]

"""

# O(log(n)) time, O(log(n)) space
# 用binarySearch方法，实现log(n)，因为整个数组是 sorted array of distinct integers
# 主要判断三种情况： 
#	如果当前value小于index，说明可以排除包括它在内的全部左边的
#	如果等于value，同时如果index == 0则肯定就是，因为index不会等于负值
#	如果等于value，同时index-1的value	小于index-1，则肯定就是，因为可以排除全部左边的
#	剩下所有情况，都可以排除全部右边的，继续递归
def indexEqualsValue(array):
	return indexEqualsValueHelper(0,len(array)-1,array)

def indexEqualsValueHelper(leftIndex,rightIndex,array):
	if leftIndex > rightIndex:
		return -1
	middleIndex = (leftIndex + rightIndex) // 2
	middleValue = array[middleIndex]
	
	if middleValue < middleIndex:
		return indexEqualsValueHelper(middleIndex + 1,rightIndex,array)
	elif middleValue == middleIndex and middleIndex == 0:
		return middleIndex
	elif middleValue == middleIndex and  array[middleIndex - 1] < middleIndex - 1:
		return middleIndex
	else:
		return indexEqualsValueHelper(leftIndex,middleIndex - 1,array)


