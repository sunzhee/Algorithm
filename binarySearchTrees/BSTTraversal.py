"""
BST Traversal
Write three functions that take in a Binary Search Tree (BST) and
an empty array, traverse the BST, add its nodes' values to the
input array, and return that array. The three functions should
traverse the BST using the in-order, pre-order, and post-order
tree-traversal techniques, respectively.
If you're unfamiliar with tree-traversal techniques, we
recommend watching the Conceptual Overview section of this
question's video explanation before starting to code.
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null .


Sample Input
tree = 10
       / \
      5  15
     / \   \
    2   5   22
   /
  1
array = []


output:

inOrderTraverse: [1, 2, 5, 5, 10, 15, 22] // where the array is the input array
preOrderTraverse: [10, 5, 2, 1, 5, 15, 22] // where the array is the input array
postOrderTraverse: [1, 2, 5, 5, 22, 15, 10] // where the array is the input array

"""


import program
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]





def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left,array)
		array.append(tree.value)
		inOrderTraverse(tree.right,array)
	return array


def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left,array)
		preOrderTraverse(tree.right,array)
	return array


def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left,array)
		postOrderTraverse(tree.right,array)
		array.append(tree.value)
	return array



