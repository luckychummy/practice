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


def is_match(p1, p2):
	if p1 == '(' and p2 == ')':
		return True
	elif p1 == '{' and p2 == '}':
		return True
	elif p1 == '[' and p2 == ']':
		return True
		return False

def isBalanced(pattern):
	index=0
	isBalanced=True
	s=Stack()

	while isBalanced and index<len(pattern):
		
		p=pattern[index]
		if p=='(' or p=='{' or p=='[':
			s.push(p)
		else:
			if not s.is_empty():
				p1=s.pop()
				if not is_match(p1, p):
					isBalanced=False
			else:
				isBalanced=False
		index+=1

	return isBalanced

print ("String : (((({})))) Balanced or not?")
print(isBalanced("(((({})))"))







		
