import sys

class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def printLL(self):
        if self.head is None:
            return
        else:
            current=self.head
            while(current):
                print(current.data)
                current=current.next
    def search(self, value):
        temp=self.head
        pos=1
        while(temp):
            if(temp.data==value):
                print("the value is found at ",pos)
            temp=temp.next
            pos+=1

    def insertAtEnd(self, info):
        if self.head is None:
            self.head=node(info)
        else:
            current=self.head
            while(current.next):
                current=current.next
            newNode=node(info)
            current.next=newNode
            newNode.next=None

def isPalindrome(llist):
        head=llist.head
        slowptr=head
        fastptr=head
        slowPrev=None
        nextHalf=None
        midNode=None

        if head is not None and head.next is not None:
            while fastptr is not None and fastptr.next is not None:
                fastptr = fastptr.next.next
                slowPrev=slowptr
                slowptr=slowptr.next

            if fastptr is not None: ##Odd number of nodes in the LinkedList
                midNode=slowptr
                slowptr=slowptr.next

            nextHalf=slowptr
            slowPrev.next=None
            nextHalf= reverse(nextHalf)
            res=compareList(head, nextHalf)
            nextHalf=reverse(nextHalf)

            if midNode is None: ##Even number of nodes in the LinkedList
                slowPrev.next=midNode
                midNode.next=nextHalf
            else:
                slowPrev.next=nextHalf
        return res

def compareList(head1, head2):
        while head1 is not None and head2 is not None:
            if head1.data==head2.data:
                head1=head1.next
                head2=head2.next

            else:
                return False

        if head1 is None and head2 is None:
            return True
        else:
            return False

def reverse(head):
        prev=None
        curr=head
        next=None

        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return curr


if __name__=='__main__':
    llist=LinkedList()
    n=int(input())
    for i in range(n):
        llist.insertAtEnd((input()))
    if isPalindrome(llist) is True:
        print("palindrome")
    else:
        print("Not palindrome")




























