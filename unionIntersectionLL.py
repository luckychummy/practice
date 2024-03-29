import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None


class LinkedList: 

    def __init__(self): 
        self.head = None


    def display(self):
        temp = self.head 
        while (temp): 
            print("{} ->".format(temp.info)),
            temp = temp.next
        print("NULL")
    
    def count(self):
        count=0
        temp=self.head
        while(temp):
            count+=1
            temp=temp.next
        return count
    
    def serach(self,value):
        temp=self.head
        pos=1
        while(temp):
            if(temp.info==value):
                print("The value found at",pos)
            temp=temp.next
            pos+=1
        print("Value not found in the linked list")
    def insert_at_beg(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.temp.next = self.head
        self.head= self.temp
    def insert_at_end(self,data):
        self.temp = node(data)
        if self.head is None:
            self.head = self.temp
            return
        self.p = self.head
        while self.p.next is not None:
            self.p=self.p.next
        self.p.next = self.temp;
        
    def insert_after_given_node(self,data,item):
        self.p=self.head
        while self.p is not None:
            if(self.p.info==item):
                self.temp=node(data)
                self.temp.next=self.p.next
                self.p.next=self.temp
                return
            self.p=self.p.next
        print("Item not found")

    def insert_at_pos(self,data,pos):
        self.temp=node(data)
        if pos==1:
            self.temp.next = self.head
            self.head= self.temp
            return
        self.p=self.head
        while pos>2 and self.p is not None:
            self.p=self.p.next
            pos-=1
        if self.p is None:
            print("Position exceeded the length of the list")
        else:
            self.temp.next=self.p.next
            self.p.next=self.temp
    def delete(self,data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.info==data:
            self.temp=self.head
            self.head=self.head.next
            return
        self.p=None
        self.curr=self.head
        while self.curr is not None:
            if self.curr.info==data:
                self.temp=self.p.next
                self.p.next=self.temp.next
                return
            self.p=self.curr
            self.curr=self.curr.next
            
def divide(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def merge(head1,head2):
    mergelist=None
    if head1==None:
        return head1
    if head2==None:
        return head2
    
    if head1.info<=head2.info:
        mergelist=head1
        head1=head1.next
    else:
        mergelist=head2
        head2=head2.next
    temp=mergelist
    while head1 and head2:
        if head1.info<=head2.info:
            temp.next=head1
            temp=temp.next
            head1=head1.next
        else:
            temp.next=head2
            temp=temp.next
            head2=head2.next
    
    if head1 is None:
        temp.next=head2
    else:
        temp.next=head1
    return mergelist
    
def mergeSort(head):
    if head and head.next:
        start_first=head
        start_second=divide(head)
        start_first = mergeSort(start_first)
        start_second = mergeSort(start_second)
        start_merged = merge(start_first, start_second)
        return start_merged
    else:
        return head

def getUnion(head1,head2):
    union=LinkedList()
    ele=0
    while(head1 is not None and head2 is not None):
        if head1.info==head2.info:
            ele=head1.info
            head1=head1.next
            head2=head2.next
        else:
            if head1.info<head2.info:
                ele=head1.info
                head1=head1.next
            else:
                ele=head2.info
                head2=head2.next
        union.insert_at_end(ele)
    while head1 is not None:
        union.insert_at_end(head1.info)
        head1=head1.next
    while head2 is not None:
        union.insert_at_end(head2.info)
        head2=head2.next
    return union.head

def getIntersection(head1,head2):
    intersect=LinkedList()
    while(head1 is not None and head2 is not None):
        if head1.info==head2.info:
            intersect.insert_at_end(head1.info)
            head1=head1.next
            head2=head2.next
        else:
            if head1.info<head2.info:
                head1=head1.next
            else:
                head2=head2.next
    return intersect.head
if __name__=='__main__':
    llist1=LinkedList()
    llist2=LinkedList()
    list1=LinkedList()
    list2=LinkedList()
    print("Enter number of elements")
    n=int(input())
    print("Enter number of elements")
    m=int(input())
    print("enter elements")
    for i in range(n):
        llist1.insert_at_end(int(input()))
    print("enter elements")
    for i in range(m):
        llist2.insert_at_end(int(input()))
    llist1.head=mergeSort(llist1.head)
    llist2.head=mergeSort(llist2.head)
    
    list1.head=getUnion(llist1.head,llist2.head)
    print("Union of list")
    list1.display()
    list2.head=getIntersection(llist1.head,llist2.head)
    print("Intersection of lists")
    list2.display()
