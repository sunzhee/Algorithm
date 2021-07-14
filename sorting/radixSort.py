"""
Radix Sort
Write a function that takes in an array of nonnegative integers and returns a sorted version
of that array. Use the Radix Sort algorithm to
sort the array.
If you're unfamiliar with Radix Sort, we
recommend watching the Conceptual Overview
section of this question's video explanation
before starting to code.

Sample Input
array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]

Sample Output
[2, 12, 65, 87, 234, 345, 654, 3008, 8762]

"""

# O(d * (n+b)) time , O(n + b) space
# d是最大数字的位数，b是0-9位数
# radix sort 必须要通过counting sort来实现，才能提高时间复杂度
# counting sort关键因素是需要直到数组最大值
# 如果radix中间用其他n*log(n)的算法实现，整体效率反而更低了。
def radixSort(array):
	if len(array) == 0:
		return array
	maxNumber = max(array)
	digit = 0
	while maxNumber / 10 ** digit > 0:
		countingSort(array,digit)
		digit += 1
	return array

def countingSort(array,digit):
	sortedArray = [0] * len(array)
	countArray = [0] * 10
	digitColumn = 10 ** digit
	
	for num in array:
		# 计算得到个位，十位，百位...等，对应位置的数字，digit=0是个位，digit=1是十位
		countIndex = (num // digitColumn) % 10
		countArray[countIndex] += 1
		
	for idx in range(1,10):
		countArray[idx] += countArray[idx - 1]
		
	# counting sort必须从末尾往前循环，是为了保证整体顺序不被破坏，正向循环走不通
	# 循环到-1，因为是开区间，所以是走到0
	for idx in reversed(range(len(array))):
		countIndex = (array[idx] // digitColumn) % 10
		countArray[countIndex] -= 1
		sortedIndex= countArray[countIndex]
		sortedArray[sortedIndex] = array[idx]
		
	for idx in range(len(array)):
		array[idx] = sortedArray[idx]
