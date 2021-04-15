"""
Invert Binary Tree

Write a function that takes in a Binary Tree and inverts it. In other
words, the function should swap every left node in the tree for its
corresponding right node.
Each BinaryTree node has an integer value , a left child
node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null .


Sample Input
tree =     1
         /   \
        2     3
       / \   / \
      4  5  6   7  
     / \
    8   9


Sample Output
           1
         /   \
        3     2
       / \   / \
      7  6  5   4
               / \
              9   8



"""



def invertBinaryTree(tree):
	#  use BFS to traverse the binary tree, while traversing, swap the children node
	queue = [tree]
	while len(queue) > 0:
		currentNode = queue.pop(0)
		#  add child node to queue, BFS traverse
		if currentNode.left is not None:
			queue.append(currentNode.left)
		if currentNode.right is not None:
			queue.append(currentNode.right)
		#  swap the left and right child
		currentNode.left,currentNode.right = currentNode.right,currentNode.left
		
	return




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None