"""
Min Height BST

Write a function that takes in a non-empty sorted array of distinct
integers, constructs a BST from the integers, and returns the root
of the BST.
The function should minimize the height of the BST.
You've been provided with a BST class that you'll have to use to
construct the BST.
Each BST node has an integer value , a left child node,
and a right child node. A node is said to be a valid BST node
if and only if it satises the BST property: its value is strictly
greater than the values of every node to its left; its value is
less than or equal to the values of every node to its right; and its
children nodes are either valid BST nodes themselves or
None / null .
A BST is valid if and only if all of its nodes are valid BST nodes.
Note that the BST class already has an insert method which
you can use if you want.


Sample Input:
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

Sample Output
          10
        /    \
       2     14
      / \    / \
     1   5  13 15
          \      \
           7     22
// This is one example of a BST with min height
// that you could create from the input array.
// You could create other BSTs with min height
// from the same array; for example:
            10
          /   \
         5    15
        / \   / \
       2   7 13  22
      /        \
     1         14


"""


def minHeightBst(array):
	return createMinHeightBst(array,None,0,len(array) - 1)

#O(n*log(n))time, because log(n)time for BST insert function
#O(n) space
def createMinHeightBst(array,bst,startIndex,endIndex):
	if startIndex > endIndex:
		return
	
	#get the middle index, round down, 
	#it doesn't matter if it is 1 index to the center left or center right,the BST finially will end up with same depth
	midIndex = (startIndex + endIndex) // 2
	#bst is None, means tree is empty, we are adding the root node
	if bst is None:
		bst = BST(array[midIndex])
	else:
		bst.insert(array[midIndex])
	#use recursive to create left child
	createMinHeightBst(array,bst,startIndex,midIndex - 1)
	#use recursive to create right child
	createMinHeightBst(array,bst,midIndex + 1,endIndex)
	
	return bst
	


def minHeightBst(array):
	return createMinHeightBST(array,0,len(array) - 1)

#O(n)time, O(n)space
def createMinHeightBST(array,startIndex,endIndex):
	#Done with construction, we reached the leaf
	if startIndex > endIndex:
		return None
	#get the middle index,divided 2, rounded down
	midIndex = (startIndex + endIndex) // 2
	#create current root node
	bst = BST(array[midIndex])
		
	bst.left = createMinHeightBST(array,startIndex,midIndex - 1)
	bst.right = createMinHeightBST(array,midIndex + 1,endIndex)
	
	return bst








#BST class construction
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)