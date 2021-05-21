"""
Largest Range

Write a function that takes in an array of
integers and returns an array of length 2
representing the largest range of integers
contained in that array.
The rst number in the output array should
be the rst number in the range, while the
second number should be the last number in
the range.
A range of numbers is dened as a set of
numbers that come right after each other in
the set of real integers. For instance, the
output array [2, 6] represents the range
{2, 3, 4, 5, 6} , which is a range of
length 5. Note that numbers don't need to be
sorted or adjacent in the input array in order
to form a range.
You can assume that there will only be one
largest range.


Sample Input
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

Sample Output
[0, 7]


"""

# O(n) time, O(n) space
# 先把所有数字加入字典，然后从字典拿出来一个，向两边扩展，看是否存在于字典中，在的话就继续扩大，直到走完，找到largest range
# 遍历的时候加入标记，这样走过的数字就不需要再走，直接跳过
def largestRange(array):
	# 用来记录起始数字和末尾数字
	bestRange = []
	# 用来记录最长的有几位
	longestLength = 0
	# 字典，用来记录全部数字
	numbers = {}
	
	for number in array:
		# 全部加入字典，同时标记为False表示还没有访问过
		numbers[number] = False
	for number in array:
		if numbers[number]:
			# 已经访问过了，不需要再展开计算，直接跳过
			continue
		numbers[number] = True
		currentLength = 1
		left = number - 1
		right = number + 1
		# 检查左边一个是否在字典里，在的话左边这个标记为访问过，当前序列长度+1，继续往左走下一个
		# 检查右边一个是否在字典里，在的话右边这个标记为访问过，当前序列长度+1，继续往右走下一个
		while left in numbers:
			numbers[left] = True
			currentLength += 1
			left -= 1
		while right in numbers:
			numbers[right] = True
			currentLength += 1
			right += 1
		# 比较当前长度和最长长度
		if currentLength > longestLength:
			longestLength = currentLength
			# 注意这里，左右一定要往回缩一格
			# 因为上面的判断不成立的时候才会跳出循环，此时index已经走到不成立的位置了
			bestRange = [left + 1, right -1]
	return bestRange
