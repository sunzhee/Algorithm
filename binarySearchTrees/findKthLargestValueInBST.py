"""
Find Kth Largest Value In BST
Write a function that takes in a Binary Search Tree (BST) and a
positive integer k and returns the kth largest integer contained
in the BST.
You can assume that there will only be integer values in the BST
and that k is less than or equal to the number of nodes in the
tree.
Also, for the purpose of this question, duplicate integers will be
treated as distinct values. In other words, the second largest
value in a BST containing values {5, 7, 7} will be 7 —not
5 .
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null 


Sample Input
tree =       15
          /      \
         5       20
        / \     / \
       2   5   17 22
      / \
     1   3
k = 3

Sample Output
17
"""


#############Solution 1################
#O(n) time, O(n) space
#use inorder BST traversal, and return all nodes to a array
#then find the Kth largest value
def findKthLargestValueInBst(tree, k):
	traversedValues = []
	inorderTravelsal(tree,traversedValues)
	
	return traversedValues[len(traversedValues) - k]
	
def inorderTravelsal(tree,traversedValues):
	if tree is None:
		return
	inorderTravelsal(tree.left,traversedValues)
	traversedValues.append(tree.value)
	inorderTravelsal(tree.right,traversedValues)



#############Solution 2################
#O(h+k) time, which h is the height of the BST, k is the kth value
#O(h) space, h is the height of the BST, because we are using recursive method
#h is same as the recursive layers.


#have to create a class to store the univarsal value.
class TreeInfo:
	def __init__(self,numberofVisited,lastestValue):
		self.numberofVisited = numberofVisited
		self.lastestValue = lastestValue
	
		
def findKthLargestValueInBst(tree, k):
	treeInformation = TreeInfo(0,0)
	reversedTraversal(tree,k,treeInformation)
	return treeInformation.latestValue
	
def reversedTraversal(node,k,treeInformation):
	if treeInformation.numberofVisited == k or node is None:
		return
	
	reversedTraversal(node.right,k,treeInformation)
	if treeInformation.numberofVisited < k:
		treeInformation.numberofVisited += 1
		treeInformation.latestValue = node.value
	reversedTraversal(node.left,k,treeInformation)



#######################################

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
