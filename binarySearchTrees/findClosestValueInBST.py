"""
Find Closest Value In BST

Write a function that takes in a Binary Search Tree (BST) and a
target integer value and returns the closest value to that target
value contained in the BST.
You can assume that there will only be one closest value.
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
      5 15
    / | / \
    2 5 13 22
   / \
  1 14

target = 12

Sample Output
13
"""

############### This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
###################




def findClosestValueInBst(tree, target):
	#tree.value is the current tree node value, here is the root
	return FnClsVlInBst(tree,target,tree.value)

def FnClsVlInBst(tree,target,closest):
	#exit the recusive, reached the end of BST
	#tree is the recusive center
	#every recursive we move 1 step deeper into tree, move left or right
	#closet is the current close value to the target
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		#find the new node value(tree.value) is close to the target, so change
		closest = tree.value
	if target > tree.value:
		#go deeper to right leaves
		return FnClsVlInBst(tree.right,target,closest)
	elif target < tree.value:
		#go deeper to left leaves
		return FnClsVlInBst(tree.left,target,closest)
	else:
		#target value equal to the tree.value(node value)
		#which means we found a node value equal to the target, and this is the closet
		return closest


"""
{
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": null, "right": null, "value": 22},
      {"id": "13", "left": null, "right": "14", "value": 13},
      {"id": "14", "left": null, "right": null, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": null, "right": null, "value": 5},
      {"id": "2", "left": "1", "right": null, "value": 2},
      {"id": "1", "left": null, "right": null, "value": 1}
    ],
    "root": "10"
  },
  "target": 12
}
"""