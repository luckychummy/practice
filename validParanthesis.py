import sys
class node: 

    def __init__(self, info): 
        self.info = info  
        self.next = None 


class Stack: 

    def __init__(self): 
        self.top = None
        
    
    def isEmpty(self):
        if self.top is None:
            return True
        return False
    
    def push(self,data):
        self.temp=node(data)
        if self.temp is None:
            print("Stack overflow")
            return
        self.temp.next=self.top
        self.top=self.temp
    
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        self.top=self.top.next    
        return d
    
    def peek(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        d=self.top.info
        return d
    def display(self):
        if self.isEmpty():
            print("Stack Underflow")
            sys.exit(0)
        self.p=self.top
        while self.p is not None:
            print(self.p.info)
            self.p=self.p.next
            
def match(a,b):
    if(a=='[' and b==']'):
        return 1
    if(a=='{' and b=='}'):
        return 1
    if(a=='(' and b==')'):
        return 1
    return 0
def checkParantheses(s):
    stack=Stack()
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            stack.push(s[i])
        if s[i]==')' or s[i]=='}' or s[i]==']':
            if stack.isEmpty():
                print("Right paranthesis are more than left ones")
                return 0
            else:
                temp=stack.pop()
                if match(temp,s[i])!=1:
                    print("Mismatched paranthesis are:{} {}".format(temp, s[i]))
                    return 0
    if stack.isEmpty()==1:
        print("Balanced Paranthesis")
        return 1
    else:
        print("Left paranthesis is more than right paranthesis")
        return 0
            
if __name__=='__main__':
    s="((a+b)+(c+d))"
    valid=checkParantheses(s)
    if valid==1:
        print("Valid Expression")
    else:
        print("Invalid Expression")
