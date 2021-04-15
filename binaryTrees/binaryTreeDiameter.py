"""
Binary Tree Diameter

Write a function that takes in a Binary Tree and returns its
diameter. The diameter of a binary tree is dened as the length
of its longest path, even if that path doesn't pass through the
root of the tree.
A path is a collection of connected nodes in a tree, where no
node is connected to more than two other nodes. The length of a
path is the number of edges between the path's rst node and its
last node.
Each BinaryTree node has an integer value , a left child
node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null .

Sample Input
tree =    1
         / \
        3   2
       / \
      7   4
     /     \
    8       5
   /         \
  9           6

Sample Output
6
// 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
// There are 6 edges between the first node and the last node of this tree's longest path.


"""


# use DFS to traverse tree, while keep two variables
#current node max height, current node max diameter

#O(n) time | O(n) space
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0,0)
	
	#  recursively going down to left and right child
	leftTreeInfo = getTreeInfo(tree.left)
	rightTreeInfo = getTreeInfo(tree.right)
	
	#  longest height of this current root
	longestPathThruRoot = leftTreeInfo.height + rightTreeInfo.height
	#  longest diameter of left and right subtree
	maxDiameterOfSubtree = max(leftTreeInfo.diameter,rightTreeInfo.diameter)
	#  current node max diameter is between:
	#longest path thru current node OR the max diameter of its subtree
	currentRootDiameter = max(longestPathThruRoot,maxDiameterOfSubtree)
	#  current node max height is max height of left or right subtree height PLUS 1
	currentRootHeight = 1 + max(leftTreeInfo.height,rightTreeInfo.height)
	
	return TreeInfo(currentRootHeight,currentRootDiameter)
	
	

#  use a class to store global values
class TreeInfo:
	def __init__(self,height,diameter):
		self.height = height
		self.diameter = diameter