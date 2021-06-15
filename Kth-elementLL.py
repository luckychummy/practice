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

	def printLL(self):
		current=self.head
		while(current):
			print(current.data)
			current=current.next

	def findKthElement(self, k):
		p=self.head
		q=self.head
		print("Kth element is")
		count=1
		while(q):
			q=q.next
			count+=1
			if count>k+1:
				p=p.next
				#print(p.data)
		print(p.data)

	def detectLoop(self):
		slow_p=self.head
		quick_p=self.head
		while (slow_p and quick_p and quick_p.next):
			slow_p=slow_p.next
			quick_p=quick_p.next.next
			if slow_p==quick_p:
				print("Loop found")
				return True
		print("No Loop detected")
		return False


ll=LinkedList()
ll.head=Node(3)

ll.insertNode(5)
ll.insertNode(6)
ll.insertNode(1)
ll.insertNode(10)
ll.printLL()

ll.findKthElement(3)
ll.insertNode(3)
#creating a loop for testing
ll.head.next.next.next.next = ll.head 
if(ll.detectLoop()): 
        print ("Found Loop")
else: 
        print ("No Loop")

