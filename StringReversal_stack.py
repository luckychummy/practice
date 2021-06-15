class Stack:

	def __init__(self):
		self.items=[]

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def is_empty(self):
		return self.items==[]

	def getStack(self):
		return self.items

def reverse_string(str):
	s=Stack()
	for i in range(len(str)):
		s.push(str[i])
	rev_str=""
	while not s.is_empty():
		rev_str+=s.pop()
	return rev_str

print("Reverse of Jai Ho is ",reverse_string("Jai Ho"))
