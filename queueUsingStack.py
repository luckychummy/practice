from queue import LifoQueue
class MyQueue(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=LifoQueue()
        self.q2=LifoQueue()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while(not self.q2.empty()):
            self.q1.put(self.q2.get())
    
        self.q2.put(x)
    
        while(not self.q1.empty()):
            self.q2.put(self.q1.get())
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.q2.get()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        item=self.q2.get()
        self.q2.put(item)
        return item

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.q2.empty()


#Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
obj.push(6)
obj.push(7)
obj.push(8)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()