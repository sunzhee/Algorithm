"""
Sum of Linked Lists

You're given two Linked Lists of potentially
unequal length. Each Linked List represents a
non-negative integer, where each node in
the Linked List is a digit of that integer, and
the rst node in each Linked List always
represents the least signicant digit of the
integer. Write a function that returns the
head of a new Linked List that represents the
sum of the integers represented by the two
input Linked Lists.
Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None /
null if it's the tail of the list. The value
of each LinkedList node is always in the
range of 0 - 9 .
Note: your function must create and return a
new Linked List, and you're not allowed to
modify either of the input Linked Lists.


Sample Input
linkedListOne = 2 -> 4 -> 7 -> 1
linkedListTwo = 9 -> 4 -> 5

Sample Output
1 -> 9 -> 2 -> 2
// linkedListOne represents 1742
// linkedListTwo represents 549
// 1742 + 549 = 2291



"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
	# 创建一个空的节点，用来标记链表头，返回值用这个头的next
	linkedListHeader = LinkedList(0)
	currentNode = linkedListHeader
	carryOver = 0
	
	# 关键判断，只要这几个有一个不满足就继续
	#while linkedListOne is not None or linkedListTwo is not None or carryOver !=0:
	# 或者反过来表达，
	while not (linkedListOne is None and linkedListTwo is None and carryOver == 0):
		valueOne = linkedListOne.value if linkedListOne is not None else 0
		valueTwo = linkedListTwo.value if linkedListTwo is not None else 0
		sumOfValue = valueOne + valueTwo + carryOver
		
		newValue = sumOfValue % 10
		newNode = LinkedList(newValue)
		currentNode.next = newNode
		currentNode = newNode
		
		carryOver = sumOfValue // 10
		linkedListOne = linkedListOne.next if linkedListOne is not None else None
		linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None
		
	return linkedListHeader.next

