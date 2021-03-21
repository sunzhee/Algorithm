def twoNumberSum(array, targetSum):

	for i in range(len(array)):
		y = targetSum -  array[i]
		if y in array and array[i] != y :
			return [array[i],y]
	return []
    

def twoNumbebSum2(array,targetSum):
	for i in range(0,len(array)):
		for j in range((i+1),len(array)):
			if array[i] + array[j] == targetSum:
				return [array[i],array[j]]
	return []


