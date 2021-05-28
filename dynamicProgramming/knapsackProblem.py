"""
Knapsack Problem
You're given an array of arrays where each
subarray holds two integer values and
represents an item; the rst integer is the
item's value, and the second integer is the
item's weight. You're also given an integer
representing the maximum capacity of a
knapsack that you have.
Your goal is to t items in your knapsack
without having the sum of their weights
exceed the knapsack's capacity, all the while
maximizing their combined value. Note that
you only have one of each item at your
disposal.
Write a function that returns the maximized
combined value of the items that you should
pick as well as an array of the indices of each
item picked.
If there are multiple combinations of items
that maximize the total value in the knapsack,
your function can return any of them.


Sample Input
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10

Sample Output

[10, [1, 3]] // items [4, 3] and [6, 7]

"""

# O(n*c) time,O(n*c) space n is itmes number, c is pack knapsack weight
def knapsackProblem(items, capacity):
	# 因为capacity我们是数字，可以直接用range，items是两个变量的list，所以需要len(items)
	knapsackValues = [[0 for x in range(0,capacity + 1)] for y in range(0,len(items) + 1)]
	#print(knapsackValues)
	for i in range(1,len(items) + 1):
		currentWeight = items[i-1][1]
		currentValue = items[i-1][0]
		for c in range(0,capacity + 1):
			 # 如果当前货物重量大于袋子容量，那么取矩阵正上方的值
				  # 如果小于，则取正上方，或者，上面一层，重量减去当前重量的值 + 当前value
					# 即是说，如果袋子容量大，那么就找之前能装下的货物和当前货物都装进来，看哪个更值钱，就保留哪个
			if currentWeight > c:
				knapsackValues[i][c] = knapsackValues[i-1][c]
			else:
				knapsackValues[i][c] = max(knapsackValues[i-1][c], knapsackValues[i-1][c-currentWeight] + currentValue)
	return [knapsackValues[-1][-1],getKnapsackItems(knapsackValues,items)]
	
def getKnapsackItems(knapsackValues,items):
	result = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1
	while i > 0:
		# 如果垂直相等，坐标往上移动一层，不添加结果集
		if knapsackValues[i][c] == knapsackValues[i-1][c]:
			i -= 1
		else:
			# 如果垂直不相等，那就添加上面的数值到结果集，同时坐标c减去上一层的重量值items[i-1][1]，找到上一层前面的坐标
			result.append(i-1)
			c -= items[i-1][1]
			i -= 1
		if c == 0:
			break
			
	return list(reversed(result))	