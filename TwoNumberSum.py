
#the best way, but only for two numbers sum
def twoNumberSum(array, targetSum):
	for i in range(len(array)):
		y = targetSum -  array[i]
		if y in array and array[i] != y :
			return [array[i],y]
	return []
    
#the simple way, use 2 x for loop
def twoNumbebSum2(array,targetSum):
	for i in range(0,len(array)):
		for j in range((i+1),len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
	return []

#left right pointer
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

