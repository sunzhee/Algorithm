"""
Maximize Expression

Write a function that takes in an array of
integers and returns the largest possible
value for the expression
array[a] - array[b] + array[c] - array
, where a , b , c , and d are indices of the
array and a < b < c < d .
If the input array has fewer than 4
elements, your function should return 0 .

Sample Input
array = [3, 6, 1, -3, 2, 7]

Sample Output
4
// Choose a = 1, b = 3, c = 4, and d = 5
// -> 6 - (-3) + 2 - 7 = 4


"""

# O(n) time, O(n) space, 
	# dynamic方法，创建四个list，第一个全都是A最大值，第二个全都是A-B最大值
	  # 第三个是A-B+C最大值，第四个是A-B+C-D最大值，最后list的最后一个就是总的公式最大值
def maximizeExpression(array):
	if len(array) < 4:
		return 0
	
	maxOfA = [array[0]] # [3] , 按照prompt的例子来看
	maxOfAMinusB = [float("-inf")] # [-inf] 到B这里，第一位肯定不存在
	maxOfAMinusBPlusC = [float("-inf")] * 2 # [-inf, -inf] C这里前两个不存在
	maxOfAMinusBPlusCMinusD = [float("-inf")] * 3 #[-inf, -inf, -inf] D是前三个都不存在
	

	for idx in range(1,len(array)):
		currentMax = max(maxOfA[idx - 1],array[idx])
		maxOfA.append(currentMax)
		
	for idx in range(1,len(array)):
		currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx - 1] - array[idx])
		maxOfAMinusB.append(currentMax)
		
	for idx in range(2,len(array)):
		currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
		maxOfAMinusBPlusC.append(currentMax)
		
	for idx in range(3,len(array)):
		currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1],maxOfAMinusBPlusC[idx - 1] - array[idx])
		maxOfAMinusBPlusCMinusD.append(currentMax)
		
	print(maxOfA)
	print(maxOfAMinusB)
	print(maxOfAMinusBPlusC)
	print(maxOfAMinusBPlusCMinusD)
	return maxOfAMinusBPlusCMinusD[ - 1]
		
		





# O(n ** 4) time, O(1) space
# 暴力破解，没啥意义
def maximizeExpression(array):
	if len(array) < 4:
		return 0
	
	maxResult = float("-inf")
	
	for a in range(len(array)):
		aValue = array[a]
		for b in range(a + 1,len(array)):
			bValue = array[b]
			for c in range(b+1,len(array)):
				cValue = array[c]
				for d in range(c+1,len(array)):
					dValue = array[d]
					expressionValue = calculateExpression(aValue,bValue,cValue,dValue)
					maxResult = max(maxResult,expressionValue)
	return maxResult

def calculateExpression(a,b,c,d):
	return a-b+c-d

