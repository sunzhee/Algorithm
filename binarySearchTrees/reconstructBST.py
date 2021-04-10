"""
Reconstruct BST
The pre-order traversal of a Binary Tree is a traversal technique
that starts at the tree's root node and visits nodes in the
following order:
1. Current node
2. Left subtree
3. Right subtree
Given a non-empty array of integers representing the pre-order
traversal of a Binary Search Tree (BST), write a function that
creates the relevant BST and returns its root node.
The input array will contain the values of BST nodes in the order
in which these nodes would be visited with a pre-order traversal.
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null 


Sample Input
preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]


Sample Output
         10
        /  \
       4   17
      / \    \
     2   5   19
    /        /
   1        18 

"""






def reconstructBst(preOrderTraversalValues):
	#when we meet leaf,leaf have only None sub nodes
	if len(preOrderTraversalValues) == 0:
		return None
	
	currentValue = preOrderTraversalValues[0]
	rightSubtreeRootIndex = len(preOrderTraversalValues)

	for index in range(1,len(preOrderTraversalValues)):
		#must be >= ,because we need think about if there are same values
		#break when we found the right index, the first value which >= than current root value.
		if preOrderTraversalValues[index] >= currentValue:
			rightSubtreeRootIndex = index
			break
			
	#left subtree is, from current root index+1(next index), to the first greater equal value of the current root value 
	leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIndex])
	#right subtree is, from first greater equal value of the current root value, to the end
	rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIndex:])
	
	#here we actually create the tree
	return BST(currentValue,leftSubtree,rightSubtree)




########################### This is an input class. Do not edit.##########################
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right