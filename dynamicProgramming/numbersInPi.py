"""
Numbers In Pi

Given a string representation of the rst n
digits of Pi and a list of positive integers (all
in string format), write a function that
returns the smallest number of spaces that
can be added to the n digits of Pi such that
all resulting numbers are found in the list of
integers.
Note that a single number can appear
multiple times in the resulting numbers. For
example, if Pi is "3141" and the numbers
are ["1", "3", "4"] , the number "1"
is allowed to appear twice in the list of
resulting numbers after three spaces are
added: "3 | 1 | 4 | 1" .
If no number of spaces to be added exists
such that all resulting numbers are found in
the list of integers, the function should
return -1 .


Sample Input
pi ="3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]

Sample Output
2 

"""

# O(n ** 3 + m) time, O(n+m) space
# n是pi的长度，m是一开始把numbers字数，和变成字典所需要的时间，为了后面计算提高速度
def numbersInPi(pi, numbers):
	numbersDict = {number: True for number in numbers}
	cache = {}
	minSpace = getMinSpaces(pi,numbersDict,cache,0)
	return -1 if minSpace == float("inf") else minSpace

def getMinSpaces(pi,numbersDict,cache,index):
	# 注意这里，不能是0，因为每次递归调用等于增加了一个空格
	  # 当到达整个字符长度时，应该是0个空格，但那里minSpacesInSuffix的+1要被抵消掉，所以这里要-1
	if index == len(pi):
		return -1
	# 缓存，减少递归计算量，提高速度
	if index in cache:
		return cache[index]
	minSpace = float("inf")
	# 从i这里切开，分成prefix和suffix
	for i in range(index,len(pi)):
		prefix = pi[index:i+1]
		if prefix in numbersDict:
			minSpacesInSuffix = getMinSpaces(pi,numbersDict,cache,i+1)
			minSpace = min(minSpace,minSpacesInSuffix + 1)
	cache[index] = minSpace
	return cache[index]
	
