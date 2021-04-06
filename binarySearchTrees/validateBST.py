"""
Validate BST
Write a function that takes in a potentially invalid Binary Search
Tree (BST) and returns a boolean representing whether the BST
is valid.
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null .
A BST is valid if and only if all of its nodes are valid BST nodes.
Sample Input

tree = 10
       / \
      5   15
     / \  / \
     2 5  13 22
    /      \
   1       14


Sample Output
true

"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return validateBSTHelper(tree,float("-inf"),float("inf"))


#O(n) time, because we need traverse all nodes
#O(d) space, d is the depth of tree, because we are using recursive
def validateBSThelper(tree,minValue,maxValue):
	if tree is None:
		return True

	if tree.value < minValue or tree.value >= maxValue:
		return False

	leftIsValid = validateBSThelper(tree.left,minValue,tree.value)
	rightIsValid = validateBSThelper(tree.right,tree.value,maxValue)

	return leftIsValid and rightIsValid