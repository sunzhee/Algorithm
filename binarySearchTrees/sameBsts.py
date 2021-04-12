"""
Same BSTs

An array of integers is said to represent the Binary Search Tree
(BST) obtained by inserting each integer in the array, from left to
right, into the BST.
Write a function that takes in two arrays of integers and
determines whether these arrays represent the same BST. Note
that you're not allowed to construct any BSTs in your code.
A BST is a Binary Tree that consists only of BST nodes. A node is
said to be a valid BST node if and only if it satises the BST
property: its value is strictly greater than the values of every node
to its left; its value is less than or equal to the values of every
node to its right; and its children nodes are either valid BST
nodes themselves or None / null .


Sample Input
arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

Sample Output
true 

both arrays represent the BST below
        10
       /  \
      8   15
     /   /  \
    5   12   94
   /    /    /
  2    11   81

"""



#  O(n^2)time and O(n^2)space
#because we need loop n*n to find the subtree array
#and we need n*n space to store the subtree array, in recursive
def sameBsts(arrayOne, arrayTwo):
	
	#if two array has different lenth, it must NOT a same BST
	if len(arrayOne) != len(arrayTwo):
		return False
	
	#  this is the main exit of the recursive method
	#subtree len is 0, means we have reached the end of the subtree array.
	#we can remove "and len(arrayTwo) == 0" because two array length is same, we write it for more readble.
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
		return True
	
	#  check if the subtree has same root node, if not, then False
	if arrayOne[0] != arrayTwo[0]:
		return False
	
	#  get sub tree array, make sure left subtree's nodes are all smaller than current subtree root node.
	#the getSmaller and GetGreaterOrEqual functions are no need to pass arrayOne[0], 
	#because we have the entire subtree array passed down, index 0 is the subtree root
	#we need make comparision with index 0, from index 1 to the end.
	leftOneSubtreeArray = getSmaller(arrayOne)
	leftTwoSubtreeArray = getSmaller(arrayTwo)
	rightOneSubtreeArray = getGreaterOrEqual(arrayOne)
	rightTwoSubtreeArray = getGreaterOrEqual(arrayTwo)
	
	#  main recursive loop, compare the left subtree to the end, and compare the right subtree to the end.
	#if all left and right subtree recursive loops return True, then it is same BST
	return sameBsts(leftOneSubtreeArray,leftTwoSubtreeArray) and sameBsts(rightOneSubtreeArray,rightTwoSubtreeArray)

	
def getSmaller(array):
	subtreeArray = []
	rootValue = array[0]
	for i in range(1,len(array)):
		if array[i] < rootValue:
			subtreeArray.append(array[i])
	return subtreeArray

def getGreaterOrEqual(array):
	subtreeArray = []
	rootValue = array[0]
	for i in range(1,len(array)):
		if array[i] >= rootValue:
			subtreeArray.append(array[i])
	return subtreeArray