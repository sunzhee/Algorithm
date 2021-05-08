"""
Linked List Construction

Write a DoublyLinkedList class that has
a head and a tail , both of which point
to either a linked list Node or None /
null . The class should support:
Setting the head and tail of the linked
list.
Inserting nodes before and after other
nodes as well as at given positions (the
position of the head node is 1 ).
Removing given nodes and removing
nodes with given values.
Searching for nodes with given values.
Note that the setHead , setTail ,
insertBefore , insertAfter ,
insertAtPosition , and remove
methods all take in actual Node s as input
parameters—not integers (except for
insertAtPosition , which also takes in
an integer representing the position); this
means that you don't need to create any new
Node s in these methods. The input nodes
can be either stand-alone nodes or nodes
that are already in the linked list. If they're
nodes that are already in the linked list, the
methods will eectively be moving the nodes
within the linked list. You won't be told if the
input nodes are already in the linked list, so
your code will have to defensively handle this
scenario.

If you're doing this problem in an untyped
language like Python or JavaScript, you may
want to look at the various function
signatures in a typed language like Java or
TypeScript to get a better idea of what each
input parameter is.
Each Node has an integer value as well
as a prev node and a next node, both of
which can point to either another node or
None / null .


Sample Usage

// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6

setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as tail

insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the node 6

insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert node with value 3 after the node 6

insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> insert stand alone node with value 3 at position 1

removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all node with value 3

remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2

containsNodeWithValue(5): true


"""

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
		# 如果没有head，说明这是一个空链表，那么head和tail都指定为即将插入的node
		# 因为只有一个元素
		if self.head is None:
			self.head = node
			self.tail = node
			return
		# 正常设置head，在当前head之前插入node
		self.insertBefore(self.head,node)

    def setTail(self, node):
		if self.tail is None:
			self.head = node
			self.tail = node
			return
		self.insertAfter(self.tail,node)

    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert
		
	# 将nodeToInsert插入到已知的node后面
    def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		# 先解除所有nodeToInsert的binding，避免它已经在链表其他位置
		self.remove(nodeToInsert)
		# 指定插入的nodeToinsert指针
		nodeToInsert.prev = node
		nodeToInsert.next = node.next
		# 因为这个是在node之后插入，所以如果node是tail的话，需要重新指定tail
		# 否则正常插入，指定指针
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		# 最后再指定node.next到nodeToInsert，否则会丢了真正后续的指针
		node.next = nodeToInsert

	# 在指定的位置position插入nodeToInsert
    def insertAtPosition(self, position, nodeToInsert):
		# 如果是在第一个位置，则相当于插入head，调用setHead方法即可
		if position == 1:
			self.setHead(nodeToInsert)
			return
		# 从head开始往下找，直到找到需要插入的position
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		# 这里已经到了需要插入的position
		# 如果不是None说明没有到tail，调用insertAfter方法
		# 否则说明到了tail，调用setTail方法
		if node is not None:
			self.insertBefore(node,nodeToInsert)
		else:
			self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
		node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
			# 上面这个node赋值，为什么不能放下面？
			#node = node.next

    def remove(self, node):
		if node == self.head:
			self.head = node.next
			#self.head = self.head.next
		if node == self.tail:
			self.tail = node.prev
			#self.tail = self.tail.prev
		self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
		node = self.head
		while node is not None and node.value != value:
			node = node.next
		# 为什么这样写？？
		return node is not None
		
	def removeNodeBindings(self,node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.prev = None
		node.next = None
		