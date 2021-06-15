import gc

class Node:
 	def __init__(self, data):
 		self.data=data
 		self.next=None
 		self.prev=None

class DoublyLinkedList:
 	def __init__(self):
 		self.head=None

 	def push(self, data): # insert a new node to the front of the list
 		newNode=Node(data)
 		
 		newNode.next=self.head

 		if self.head is not None:
 			self.head.prev = newNode

 		self.head=newNode

 	def insertAfter(self, positionNode, data):
 		if positionNode is None:
 			return

 		newNode=Node(data)
 		newNode.next=positionNode.next
 		positionNode.next=newNode
 		newNode.prev=positionNode
 		if newNode.next is not None:
 			newNode.next.prev=newNode

 	def append(self, data):
 		newNode=Node(data)
 		newNode.next=None
 		if(self.head is None):
 			newNode.prev=None
 			self.head=newNode
 			return

 		last=self.head
 		while(last.next is not None):
 			last=last.next
 		last.next=newNode
 		newNode.prev=last
 		return

 	def printDLL(self):
 		last = self.head
 		print ("Traversing in forward direction")
 		while(last is not None):
 			print (last.data)
 			node=last
 			last=last.next
 		print ("traversing in backward direction")
 		while(node is not None):
 			print (node.data)
 			node=node.prev

 	def deleteNode(self, dataNode):
 		if(self.head is None or dataNode is None):
 			return
 		if(self.head==dataNode):
 			self.head=dataNode.next
 			
 		if(dataNode.next is not None):
 			dataNode.next.prev=dataNode.prev

 		if(dataNode.prev is not None):
 			dataNode.prev.next=dataNode.next

 		gc.collect()

 	def deleteNodeAtGivenPos(self, head_ref, n):
 		if (head_ref == None or n<=0):
 			return
 		current = head_ref
 		i=1

 		while(current is not None and i<n):
 			current = current.next
 			i+=1

 		if(current==None):
 			return

 		self.deleteNode(current)

 		return(head_ref)





# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
llist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 
  
print ("Created DLL is: ", 
llist.printDLL() )


# delete nodes from doubly linked list 
llist.deleteNode(llist.head) 
llist.deleteNodeAtGivenPos(llist.head, 4) 
#dll.deleteNode(dll.head.next) 
# Modified linked list will be NULL<-8->NULL 
print ("\n Modified Linked List"), 
llist.printDLL() 