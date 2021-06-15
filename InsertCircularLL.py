#Check for leetcode - interviewPrep
#Definition of Node
# class Node(object):
# 	def __init__(self, val=None, next=None):
# 		self.val=val
# 		self.next=next


class Solution(object):
	def insert(self, head, insertVal):
		if head==None:
			newNode=Node(insertVal, None)
			newNode.next=newNode
			return newNode

		while True:

			prev, current=head, head.next
			toInsert=False
			if prev.val <=insertVal <= current.val:
				toInsert=True


			#case2 
			elif prev.val>current.val:
				if prev.val>insertval or current.val > insertVal:
					toInsert=True

			if toInsert:
				prev.next=Node(insertVal, current)
				return head

			prev, current=current, current.next


			if prev==head:
				break

		#Case 3: (All numbers in the Linkedlist are same/equal)
		prev.next=Node(insertVal, current)
		return head

