"""
Max Path Sum In BinaryTree

Write a function that takes in a Binary Tree
and returns its max path sum.
A path is a collection of connected nodes in a
tree, where no node is connected to more
than two other nodes; a path sum is the sum
of the values of the nodes in a particular path.
Each BinaryTree node has an integer
value , a left child node, and a right
child node. Children nodes can either be
BinaryTree nodes themselves or None /
null .
Sample Input

tree = 1
	  / \
     2   3
    / \ / \
   4  5 6  7


Sample Output
18 // 5 + 2 + 1 + 3 + 7
"""


def maxPathSum(tree):
	_,maxSum = findMaxPathSum(tree)
	return maxSum

# O(n) time, O(n) space
# 主要复杂在于要考虑到右的节点可能是负值，需要抛弃这个节点
      # 针对一个节点，有四种情况的最大值，单独root点，root+左，root+右，左+root+右
      # 前三个为maxSumAsBranch，最后一个为maxSumAsRootNode
def findMaxPathSum(tree):
	# base case, we are on leaf
	# -inf which is when all node value is nagative, we cannot return 0
	if tree is None:
		return (0,float("-inf"))
	
	leftMaxSumAsBranch,leftMaxPathSum = findMaxPathSum(tree.left)
	rightMaxSumAsBranch,rightMaxPathSum = findMaxPathSum(tree.right)
	#maxChildSumAsBranch = max(leftMaxSumAsBranch,rightMaxSumAsBranch) 
	value = tree.value
	# 如果left  branch或者right branch是负值，那就只用node value
	maxSumAsBranch = max((leftMaxSumAsBranch + value), (rightMaxSumAsBranch + value), value) 
	# 算上root的整个大三角形 ，或者是上面的某一个branch
	maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch,maxSumAsBranch) 
	# 要么是左child里的三角形，要么是右child里的三角形，要么是整个三角形
	maxPathSum = max(leftMaxPathSum,rightMaxPathSum,maxSumAsRootNode) 
	
	return (maxSumAsBranch,maxPathSum)
