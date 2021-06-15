class Node:
	def __init__(self, data):
		self.data=data
		self.prev=None
		self.next=None

class CircularLinkedList:
	def __init__(self):
		self.head=None

	def getNode(self, index):
		current = self.head
		for i in range(index):
			current=current.next
			if(current==self.head):
				return None
		return current

	def insertAfter(self, posNode, newNode):
		newNode.next=posNode.next
		newNode.prev=posNode
		posNode.next=newNode
		newNode.next.prev=newNode

	def insertBefore(self, posNode,newNode):
		self.insertAfter(posNode.prev, newNode)

	def insertAtEnd(self, newNode):
		if (self.head is None):
			self.head=newNode
			newNode.next=newNode
			newNode.prev=newNode
		else:
			self.insertAfter(self.head.prev, newNode)

	def insertAtBeg(self, newNode):
		self.insertAtEnd(newNode)
		self.head(newNode)

	def delete(self, node):
		if self.head==node:
			self.head=node.next
		else:
			node.next.prev=node.prev
			node.prev.next=node.next

	def sortedCLLInsert(self, node):
		current=self.head
		while(current.next):
			if(node.data>current.prev.data and node.data<current.data):
				current.next=node
				node.next=current.next
				node.prev=current
				current.next.prev=node


	def printCll(self):
		if self.head is None:
			return
		current=self.head
		while(current.next):
			print(current.data)
			current=current.next
			if current==self.head:
				break

ccList = CircularLinkedList()

ccList.push(12)
ccList.push(1)
ccList.push(17)
ccList.push(2)

ccList.printCLL()