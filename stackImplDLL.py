class Node:
	def __init__(self, data):
		self.data=data
		self.next=None
		self.prev=None

class Stack:
	def __init__(self):
		self.head=None

	def push(self, data):
		if self.head==None:
			newNode=Node(data)
			self.head=newNode
		else:
			newNode=Node(data)
			self.head.prev=newNode
			newNode.next=self.head
			#self.head.next.prev=newNode
			self.head=newNode
			newNode.prev=None

	def pop(self):
		if self.head is None:
			return
		elif self.head.next is None:
			tmp=self.head.data
			self.head=None
			return tmp
		else:
			tmp=self.head
			self.head=tmp.next
			self.head.prev=None
			return tmp.data

	def top(self):
		return self.head.data

	def size(self):
		count=1
		if self.head is not None:
			current=self.head
			while(current.next):
				current=current.next
				count+=1

		return count

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def printStack(self):
		if self.head is None:
			return True
		current=self.head
		while(current):
			print(current.data)
			current=current.next

	# Code execution starts here          
if __name__=='__main__':  
  
# Start with the empty stack 
  stack = Stack() 
  
# Insert 4 at the beginning. So stack becomes 4->None  
  print("Stack operations using Doubly LinkedList") 
  stack.push(4) 
  
# Insert 5 at the beginning. So stack becomes 4->5->None  
  stack.push(5) 
  
# Insert 6 at the beginning. So stack becomes 4->5->6->None  
  stack.push(6) 
  
# Insert 7 at the beginning. So stack becomes 4->5->6->7->None  
  stack.push(7) 
  
# Print the stack 
  stack.printStack() 
  
# Print the top element 
  print("\nTop element is ", stack.top()) 
  
# Print the stack size 
  print("Size of the stack is ", stack.size()) 
  
# pop the top element 
  stack.pop() 
  
# pop the top element 
  stack.pop() 
    
# two elements are popped 
# Print the stack 
  stack.printStack() 
    
# Print True if the stack is empty else False 
  print("\nstack is empty:", stack.isEmpty()) 
  
