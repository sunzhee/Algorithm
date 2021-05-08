"""
Reverse Linked List

Write a function that takes in the head of a
Singly Linked List, reverses the list in place
(i.e., doesn't create a brand new list), and
returns its new head.
Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None / null
if it's the tail of the list.
You can assume that the input Linked List will
always have at least one node; in other
words, the head will never be None / null
.
Sample Input
0 -> 1 -> 2 -> 3 -> 4 -> 5 

Sample Output
5 -> 4 -> 3 -> 2 -> 1 -> 0 
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	p1,p2 = None,head
	while p2 is not None:
		# 一定要放在这里，如果放在最后的话，会出现p2已经是None,
		# 然后下一步给p3赋值时，None.next 会出错，要加if语句来避免语法错误
		# 这样写最简单明了
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
	return p1
