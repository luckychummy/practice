class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next

class LinkedList:
	def __init__(self):
		self.head=None

	def insertNode(self, data):
		newNode=Node(data)
		if(self.head):
			current=self.head
			while(current.next):
				current=current.next
			current.next=newNode
		else:
			self.head=newNode

	def deleteNode(self, key):
		tmp=self.head
		if(tmp is not None and tmp.data==key):
			self.head=tmp.next
			tmp=None
			return

		while (tmp is not None):
			if tmp.data==key:
				break
			prev=tmp
			tmp=tmp.next
		prev.next=tmp.next
		tmp=None

		if tmp==None:
			return


	def printLL(self):
		current=self.head
		while(current):
			print(current.data)
			current=current.next

ll=LinkedList()
ll.head=Node(3)

ll.insertNode(5)
ll.insertNode(6)
ll.insertNode(1)
ll.insertNode(10)

ll.printLL()
#print(ll.head.data)
ll.deleteNode(5)
ll.printLL()

