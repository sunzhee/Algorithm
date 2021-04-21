"""
Height Balanced Binary Tree

You're given the root node of a Binary Tree. Write a function that
returns true if this Binary Tree is height balanced and false
if it isn't.
A Binary Tree is height balanced if for each node in the tree, the
dierence between the height of its left subtree and the height of
its right subtree is at most 1 .
Each BinaryTree node has an integer value , a left child
node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null .


Sample Input
tree =    1
        /   \
       2     3
      / \     \
     4   5     6
        / \
       7   8

 Sample Output
 True


O(n) time | O(h) space, h is the height of the tree
"""



#class must define before this calss instance call
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.right.right = BinaryTree(6)
tree.left.right.left = BinaryTree(7)
tree.left.right.right = BinaryTree(8)

		
class TreeInfo:
	def __init__(self,isBalanced,height):
		self.isBalanced = isBalanced
		self.height = height

######### end of input ######


def heightBalancedBinaryTree(tree):
	treeInfo = checkBalanceTree(tree)
	return treeInfo.isBalanced

#recursive call, need two value, the node is balanced or not and the node's height
#store it in a class called TreeInfo, every recursive call, we create a class instance,
def checkBalanceTree(tree):
	if tree is None:
		#return value is a class, so we use calss name to define it.
		return TreeInfo(True,0)
	
	leftTreeInfo = checkBalanceTree(tree.left)
	rightTreeInfo = checkBalanceTree(tree.right)
	
	balanced = (leftTreeInfo.isBalanced
				and rightTreeInfo.isBalanced
				and (abs(leftTreeInfo.height - rightTreeInfo.height) <= 1)
			   )
	
	height = max(leftTreeInfo.height,rightTreeInfo.height) + 1
	
	return TreeInfo(balanced,height)

print("output:",heightBalancedBinaryTree(tree))