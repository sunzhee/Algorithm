"""
Next Greater Element

Write a function that takes in an array of
integers and returns a new array containing,
at each index, the next element in the input
array that's greater than the element at that
index in the input array.
In other words, your function should return a
new array where outputArray[i] is the
next element in the input array that's greater
than inputArray[i] . If there's no such
next greater element for a particular index,
the value at that index in the output array
should be -1 . For example, given
array = [1, 2] , your function should
return [2, -1] .
Additionally, your function should treat the
input array as a circular array. A circular
array wraps around itself as if it were
connected end-to-end. So the next index
after the last index in a circular array is the
rst index. This means that, for our problem,
given
array = [0, 0, 5, 0, 0, 3, 0 0] ,
the next greater element after 3 is 5 ,
since the array is circular.


Sample Input
array = [2, 5, -3, -4, 6, 7, 2]

Sample Output
[5, 6, 6, 6, 7, -1, 5]



"""
# O(n) time, O(n) space
def nextGreaterElement(array):
	result = [-1] * len(array) 
	stack = []
	
	# 从右向左遍历两遍
	for idx in range(2 * len(array) - 1,-1,-1):
		circularIdx = idx % len(array)
		
		# 查看stack里面的最大值，如果当前值大于等于stack的最后一个数字，那么堆栈最后一个pop掉，
        #     直到堆栈值大于等于或者pop空为止
		# 否则，返回结果数组，当前值应该就是堆栈的最后一个数字stack[len(stack) - 1]
		while len(stack) > 0:
			if stack[len(stack) - 1] <= array[circularIdx]:
				stack.pop()
			else:
				result[circularIdx] = stack[len(stack) - 1]
				break
		# 当前循环完毕，把当前值加入堆栈
		stack.append(array[circularIdx])
	return result
