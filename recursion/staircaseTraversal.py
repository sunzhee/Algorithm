"""
Staircase Traversal

You're given two positive integers
representing the height of a staircase and
the maximum number of steps that you can
advance up the staircase at a time. Write a
function that returns the number of ways in
which you can climb the staircase.
For example, if you were given a staircase of
height = 3 and maxSteps = 2 you
could climb the staircase in 3 ways. You
could take 1 step, 1 step, then 1 step, you
could also take 1 step, then 2 steps, and
you could take 2 steps, then 1 step.
Note that maxSteps <= height will
always be true.


Sample Input
height = 4
maxSteps = 2


Sample Output
5
// You can climb the staircase in the fo
// 1, 1, 1, 1
// 1, 1, 2
// 1, 2, 1
// 2, 1, 1
// 2, 2

"""
#####################
# Solution 1
#####################
def staircaseTraversal(height, maxSteps):
	return numberOfWaysToTop(height,maxSteps)

# 解法是扩展版的斐波那契数列，fibonacci是前两个数之和，这个是前maxStep之和
# O(m^h) time, m is maxStep, h is staircase height
# O(h) space
def numberOfWaysToTop(height,maxStep):
	numberOfWays = 0
	if height <= 1:
		return 1
	# 从1到最大步数循环，要从最高点减去步数1，步数2...直到减去最大步数，将这些结果累加
	# 需要+1是因为range是开区间，我们需要包括最大步数，所以最后一个循环要+1
	for step in range(1,min(height,maxStep) + 1):
		numberOfWays += numberOfWaysToTop(height - step,maxStep)
	return numberOfWays

	
#####################
# Solution 2
#####################
# O(m*h) time,h is height, m is maxStep, O(h) space
def staircaseTraversal(height, maxSteps):
	# 基本条件，到达台阶0需要1步，台阶1需要1步
	memo ={
		0:1,
		1:1,
	}
	return waysToTop(height,maxSteps,memo)

def waysToTop(height,maxSteps,memo):
	# 如果已经在base case里，或者计算过了，直接调用
	if height in memo:
		return memo[height]
	
	numberOfWays = 0
	for step in range(1,min(height,maxSteps) + 1):
		numberOfWays += waysToTop(height - step,maxSteps,memo)
	# 这一层递归完成，记录下来到达这个高度需要的步数，用来以后调用
	memo[height] = numberOfWays
	
	return numberOfWays
