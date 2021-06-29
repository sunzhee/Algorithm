"""
Validate Three Nodes
You're given three nodes that are contained in the same Binary
Search Tree: nodeOne , nodeTwo , and nodeThree . Write a
function that returns a boolean representing whether one of
nodeOne or nodeThree is an ancestor of nodeTwo and the
other node is a descendant of nodeTwo . For example, if your
function determines that nodeOne is an ancestor of nodeTwo ,
then it needs to see if nodeThree is a descendant of
nodeTwo . If your function determines that nodeThree is an
ancestor, then it needs to see if nodeOne is a descendant.
A descendant of a node N is dened as a node contained in
the tree rooted at N . A node N is an ancestor of another node
M if M is a descendant of N .
It isn't guaranteed that nodeOne or nodeThree will be
ancestors or descendants of nodeTwo , but it is guaranteed that
all three nodes will be unique and will never be None / null .
In other words, you'll be given valid input nodes.
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null


tree =     5
        /     \
       2       7
      / \     / \
     1   4   6   8
    /   /
   0   3

// This tree won't actually be passed as an input
nodeOne = 5 // The actual node with value 5.
nodeTwo = 2 // The actual node with value 2.
nodeThree = 3 // The actual node with value 3.

Sample output 
True

"""

#import program
#import unittest

# This is an input class. Do not edit.
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


root = BST(5)
root.left = BST(2)
root.right = BST(7)
root.left.left = BST(1)
root.left.left.left = BST(0)
root.left.right = BST(4)
root.left.right.left = BST(3)
root.right.left = BST(6)
root.right.right = BST(8)

nodeOne = root
nodeTwo = root.left
nodeThree = root.left.right.left






def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	#  check if the nodeTwo is nodeOne's descendant, return True or False
	#check whether 1->2 is True
	#if first check 1->2 is False, we don't need check second 2->3, just return False
	if isDescendant(nodeOne,nodeTwo):
		#  reverse the input position, then we can check ancestor
		#here we check if nodeThree is nodeTwo's descendant
		#check whether 2->3 is True
		return isDescendant(nodeTwo,nodeThree)
	
	#the reverse situation of above, check whether 3->2 is True
	if isDescendant(nodeThree,nodeTwo):
		#check whether 2->1 is True
		return isDescendant(nodeTwo,nodeOne)
	
	#  if both above is not the case,which means 3 numbers are not in ancestor relation
	#so return False
	return False
	
#check whether the "target" is descendant of "node"
def isDescendant(node,target):
	#  we reach the bottom leaf, not able to find target node, so return False
	if node is None:
		return False
	
	#  we find the target node
	if node == target:
		return True
	
	#if target.value < node.value:
	#	return isDescendant(node.left,target)
	#else:
	#	return isDescendant(node.right,target)
	
	#  same as above, just one line code
	#recursivly go left child if target value is less then current node value
	#otherwise recursivly go right child, until we reach the leaf or target node
	return isDescendant(node.left,target) if target.value < node.value else isDescendant(node.right,target)




print("nodeOne=",nodeOne.value,"\nnodeTwo=",nodeTwo.value,"\nnodeThree=",nodeThree.value)
print("output:",validateThreeNodes(nodeOne, nodeTwo, nodeThree))


