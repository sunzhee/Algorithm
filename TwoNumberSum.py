def twoNumberSum(array, targetSum):

	for i in range(len(array)):
		y = targetSum -  array[i]
		if y in array and array[i] != y :
			return [array[i],y]
	return []
    

