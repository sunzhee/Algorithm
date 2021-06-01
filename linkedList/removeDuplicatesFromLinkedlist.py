"""
Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in
sorted order with respect to their values. Write a function that
returns a modied version of the Linked List that doesn't contain
any nodes with duplicate values. The Linked List should be
modied in place (i.e., you shouldn't create a brand new list), and
the modied Linked List should still have its nodes sorted with
respect to their values.
Each LinkedList node has an integer value as well as a
next node pointing to the next node in the list or to None /
null if it's the tail of the list.


Sample Input
linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1

Sample Output
1 -> 3 -> 4 -> 5 -> 6 // the head node with value 1

"""

# This is an input class. Do not edit.
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


#O(n) time, O(1)space
def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	#it is a sorted linked list, so just check if there is continues same number
	#if yes, move next, until find a distinct number, then point to it
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and currentNode.value == nextDistinctNode.value:
			nextDistinctNode = nextDistinctNode.next
		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode
	return linkedList



