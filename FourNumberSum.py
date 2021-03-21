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
		




print (fourNumberSum(array,targetSum))