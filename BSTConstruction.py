"""
BST Construction
Write a BST class for a Binary Search Tree. The
class should support:
Inserting values with the insert method.
Removing values with the remove method;
this method should only remove the rst
instance of a given value.
Searching for values with the contains
method.
Note that you can't remove values from a singlenode tree. In other words, calling the remove
method on a single-node tree should simply not do
anything.
Each BST node has an integer value , a left
child node, and a right child node. A node is said
to be a valid BST node if and only if it satises the
BST property: its value is strictly greater than the
values of every node to its left; its value is less
than or equal to the values of every node to its right;
and its children nodes are either valid BST nodes
themselves or None / null .



"""

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
		currentNode = self
		while True:
			#insert value less than current node, then go left
			if value < currentNode.value:
				#if None, means current node left child is none, we add value here
				if currentNode.left is None:
					#add value to current node's left child,and break the while loop
					currentNode.left = BST(value)
					break
				#if not None, we need to deeper
				else:
					currentNode = currentNode.left
			else:
				#insert value greater than current node, then go right
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
		#if we didnt meet the end leaf of the tree
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				#the value equal to currentNode.value,we found it
				return True
        return False

    def remove(self, value,parentNode = None):
		currentNode = self
		#go deeper, find the node, until meet None(leaf)
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			#we found the node
			else:
				#the node has two children
				if currentNode.left is not None and currentNode.right is not None:
					#get the minium value from right sub tree to replace this node
					#and then remove the minum value node from right sub tree
					#call this remove method in the class again, one layer recursive
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value,currentNode)
				elif parentNode is None: #we are removing the root node
					if currentNode.left is not None:
						#becareful here, for the left child, we must deal with right child first
						#if we do left child first, it will cause error, can not find the right child value
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						#same as above, for right child, need to do the left child first, otherwise will cause error
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						#this is a single-node tree, do nothing
						pass
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break

        return self

	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value