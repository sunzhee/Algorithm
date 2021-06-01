"""
Remove Kth Node From End
Write a function that takes in the head of a
Singly Linked List and an integer k and
removes the kth node from the end of the
list.
The removal should be done in place,
meaning that the original data structure
should be mutated (no new structure should
be created).
Furthermore, the input head of the linked list
should remain the head of the linked list
after the removal is done, even if the head is
the node that's supposed to be removed. In
other words, if the head is the node that's
supposed to be removed, your function
should simply mutate its value and
next pointer.
Note that your function doesn't need to
return anything.
You can assume that the input Linked List
will always have at least two nodes and,
more specically, at least k nodes.
Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None /
null if it's the tail of the list.

Sample Input:

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
k = 4

Sample Output:
// No output required.
// The 4th node from the end of the list 6, is removed
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	firstNode = head
	secondNode = head
	counter = 1
	while counter <= k:
		secondNode = secondNode.next
		counter += 1
	# 如果是None，说明k等于linkedlist总长度，需要把head删除掉
	# 同时创建一个新的head
	if secondNode == None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while secondNode.next != None:
		secondNode = secondNode.next
		firstNode = firstNode.next
	firstNode.next = firstNode.next.next
	
