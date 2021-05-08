"""
Merge Linked Lists

Write a function that takes in the heads of
two Singly Linked Lists that are in sorted
order, respectively. The function should
merge the lists in place (i.e., it shouldn't
create a brand new list) and return the head
of the merged list; the merged list should be
in sorted order.
Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None / null
if it's the tail of the list.
You can assume that the input linked lists will
always have at least one node; in other
words, the heads will never be None / null .


Sample Input
headOne = 2 -> 6 -> 7 -> 8 
headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 

Sample Output
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
"""
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	p1 = headOne
	p2 = headTwo
	p1Prev = None
	while p1 is not None and p2 is not None:
		# 因为p1小，所以不需要改变链表，p1直接走到下一个Node
		if p1.value < p2.value:
			p1Prev = p1
			p1 = p1.next
		# p1大于p2，所以需要把p2插入到p1的前面，同时也要插入p1Prev的后面
		else: #if p1.value > p2.value: 这里不能用if，必须else来进入条件，因为当p1走完的时候，不可能大于p2，
				#这时候所有if的语句无法执行，指针不走，陷入死循环
			# 当p1是head的时候，p1Prev是None，过滤掉这种情况，同时这时候也不需要修改p1Prev的指针
			if p1Prev is not None:
				p1Prev.next = p2
			p1Prev = p2
			p2 = p2.next
			p1Prev.next = p1
			
	# 如果p2还剩下node，p1已经走完，则需要修改pointer，把最后一个连接指向p2
	# 如果p1还剩下node，p2已经走完，则不需要任何修改动作
	if p1 is None:
		p1Prev.next = p2
	# 需要考虑一下最后链表头是哪个数值，哪个小哪个就是头
	return headOne if headOne.value < headTwo.value else headTwo
			
			
			
