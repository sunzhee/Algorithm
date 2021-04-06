
"""
Depth-frst Search

You're given a Node class that has a name and an array of
optional children nodes. When put together, nodes form an
acyclic tree-like structure.
Implement the depthFirstSearch method on the Node
class, which takes in an empty array, traverses the tree using the
Depth-rst Search approach (specically navigating the tree from
left to right), stores all of the nodes' names in the input array,
and returns it.
If you're unfamiliar with Depth-rst Search, we recommend
watching the Conceptual Overview section of this question's
video explanation before starting to code.

Sample Input
graph = A
      / | \
      B C D
     / \ / \
     E F G H
      / \ \
      I J K

Sample Output

["A", "B", "E", "F", "I", "J", "C", "D", "G", "K"]

"""





# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, resultArray):
		#add node name to result array
        resultArray.append(self.name)
		#loop thru the children of current node, one by one
		#call this Node calss own method, on current node's child , recursivly
		#no need an "if is not None" to check current node is leaf or not
		#because if it is leaf, it will go out of the loop, then return
		for child in self.children:
			child.depthFirstSearch(resultArray)
		return resultArray