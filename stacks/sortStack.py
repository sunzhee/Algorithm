"""
Sort Stack

Write a function that takes in an array of
integers representing a stack, recursively
sorts the stack in place (i.e., doesn't create a
brand new array), and returns it.
The array must be treated as a stack, with the
end of the array as the top of the stack.
Therefore, you're only allowed to
Pop elements from the top of the stack
by removing elements from the end of
the array using the built-in .pop()
method in your programming language
of choice.
Push elements to the top of the stack
by appending elements to the end of
the array using the built-in
.append() method in your
programming language of choice.
Peek at the element on top of the stack
by accessing the last element in the
array.
You're not allowed to perform any other
operations on the input array, including
accessing elements (except for the last
element), moving elements, etc.. You're also
not allowed to use any other data structures,
and your solution must be recursive.


Sample Input
stack = [-5, 2, -2, 4, 3, 1]


Sample Output
[-5, -2, 1, 2, 3, 4]


"""
# O(n^2) time, O(n) space
def sortStack(stack):
	# base case，全都pop空了以后，[]也是sorted stack，所以才可以返回
	if len(stack) == 0:
		return stack
		
	top = stack.pop()
	sortStack(stack)
	# 到这里stack已经空了，开始插入
	insertSortedStack(stack,top)
	return stack

def insertSortedStack(stack,value):
	# base case，如果是空，或者当前待插入值大于等于stack上面的值，可以直接append，否则要往下继续调用递归
	if len(stack) == 0 or stack[-1] <= value:
		stack.append(value)
		return
	# 先pop出来最上面的，然后继续把当前值往里插入，调用递归
	top = stack.pop()
	insertSortedStack(stack,value)
	# 上面pop完之后，这里top肯定大于stack最上面的值，直接插入即可，保证stack仍旧是sorted
	stack.append(top)
	
