"""


Breadth-frst Search
You're given a Node class that has a name and an array of
optional children nodes. When put together, nodes form an
acyclic tree-like structure.
Implement the breadthFirstSearch method on the Node
class, which takes in an empty array, traverses the tree using the
Breadth-rst Search approach (specically navigating the tree
from left to right), stores all of the nodes' names in the input
array, and returns it.
If you're unfamiliar with Breadth-rst Search, we recommend
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

["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]

"""

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
		while len(queue) > 0:
			currentNode = queue.pop(0)
			array.append(currentNode.name)
			for i in currentNode.children:
				queue.append(i)
		return array
