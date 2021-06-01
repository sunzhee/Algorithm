"""
Shift Linked List
Write a function that takes in the head of a
Singly Linked List and an integer k , shifts
the list in place (i.e., doesn't create a brand
new list) by k positions, and returns its new
head.
Shifting a Linked List means moving its
nodes forward or backward and wrapping
them around the list where appropriate. For
example, shifting a Linked List forward by
one position would make its tail become the
new head of the linked list.
Whether nodes are moved forward or
backward is determined by whether k is
positive or negative.
Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None / null if it's the tail of the list.
You can assume that the input Linked List
will always have at least one node; in other
words, the head will never be None / null .

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5
k = 2

Sample Output
4 -> 5 -> 0 -> 1 -> 2 -> 3

"""

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
	# 如果k为0，则不动
	if k == 0:
		return head
	listLength = 1
	listTail = head
	# 计算链表长度，找到链表尾
	while listTail.next is not None:
		listTail = listTail.next
		listLength += 1
	# 如果能整除，余数为0，则不动
	if abs(k) % listLength == 0:
		return head
	# 计算新的链表tail位置，如果k为正数，则用长度减去%取余，如果k为负数，就是%取余
	newTailPosition = (listLength - abs(k) % listLength) if k > 0 else abs(k) % listLength
	# 找出newTail
	newTail = head
	for i in range(1,newTailPosition):
		newTail = newTail.next
		
	# 现在四个关键位置都有了，开始操作
	# head, listTail, newTail, newHead(newTail.next)
	listTail.next = head
	newHead = newTail.next
	newTail.next = None
	
	return newHead

