# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

#  Input: 1 1


#    / \ / \


#   2 3 2 3

# [1,2,3], [1,2,3]

# Output: true
import sys
class Node:

	def __init__(self, val):
		self.val=val
		self.left=None
		self.right=None

def insert(pt, key):
	if pt is None:
		pt=Node(key)
	elif (key <=pt.val):
		pt.left=insert(pt.left, key)
	elif (key >=pt.val):
		pt.right=insert(pt.right, key)
	return pt

def checkIdentical(p1, p2):
	if p1 is None and p2 is None:
		return True
	if p1 is None or p2 is None:
		return False
	return p1.val==p2.val and checkIdentical(p1.left,p2.left) and checkIdentical(p1.right,p2.right)



if __name__ == '__main__':
	root1=None
	root2=None

	root1=insert(root1, 10)
	root1=insert(root1, 20)
	root1=insert(root1, 30)
	root1=insert(root1, 40)
	root1=insert(root1, 60)

	root2=insert(root2, 10)
	root2=insert(root2, 20)
	root2=insert(root2, 30)
	root2=insert(root2, 40)
	root2=insert(root2, 50)

	if checkIdentical(root1, root2):
		print("Trees are identical")
	else:
		print("Trees are not same")



