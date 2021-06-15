class Node:
	def __init__(self, data):
		self.data=data
		self.next=None
		self.prev=None

class Queue:
	def __init__(self):
		self.head=None
		self.last=None

	def enqueue(self, data):
		if self.last is None:
			self.head=Node(data)
			self.last=self.head
		else:
			self.last.next=Node(data)
			self.last=self.last.next

	def dequeue(self):
		if self.head is None:
			return None
		else:
			tmp = self.head
			self.head=self.head.next
			self.head.prev=None
			return tmp

	def first(self):
		return self.head.data

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def printqueue(self):
		if self.head is None:
			return
		else:
			current=self.head
			while(current):
				print(current.data)
				current=current.next

	def size(self):
		if self.head is None:
			return
		else:
			current=self.head
			count=0
			while(current):
				count+=1
				current=current.next
		return count

# Code execution starts here           
if __name__=='__main__':  
   
# Start with the empty queue 
  queue = Queue() 
   
  print("Queue operations using doubly linked list") 
   
# Insert 4 at the end. So queue becomes 4->None   
  queue.enqueue(4) 
   
# Insert 5 at the end. So queue becomes 4->5None   
  queue.enqueue(5) 
   
# Insert 6 at the end. So queue becomes 4->5->6->None   
  queue.enqueue(6) 
   
# Insert 7 at the end. So queue becomes 4->5->6->7->None   
  queue.enqueue(7) 
   
# Print the queue  
  queue.printqueue() 
   
# Print the first element  
  print("\nfirst element is ",queue.first()) 
   
# Print the queue size  
  print("Size of the queue is ",queue.size()) 
   
# remove the first element  
  queue.dequeue() 
   
# remove the first element  
  queue.dequeue() 
   
# first two elements are removed 
# Print the queue  
  print("After applying dequeue() two times") 
  queue.printqueue() 
   
# Print True if queue is empty else False  
  print("\nqueue is empty:",queue.isEmpty())


