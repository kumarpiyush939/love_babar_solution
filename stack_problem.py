

# Implement Stack from Scratch




class mystack():
    
    def __init__(self) -> None:
        self.items=[]
        
    def is_empty(self) -> bool:
        return self.items == []
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else : 
            return "stack is empty!"
    
    def push(self, item):
        self.items.append(item)
        return self.items
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
#TODO implement stack with linked list 
    
# sk=mystack()
# print(sk)
# print(sk.is_empty())
# print(sk.pop())
# print(sk.push(5))
# print(sk.push(5))
# print(sk.push(5))
# print(sk.push(5))
# print(sk.size())
# print(sk.pop())
# print(sk.peek())

# Implement Queue from Scratch

class myQueue():
    def __init__(self) -> None:
        self.q=[]
        
    def enqueue(self, item):
        self.q.insert(0, item)
        
    def dequeue(self):
        return self.q.pop()

    def is_empty(self):
        return self.q ==[]
    
    def size(self):
        return len(self.q)

# myq = 
import array


#Implement 2 stack in an array



class twoStack():
    def __init__(self, n) -> None:
        self.size = n
        self.items = [None] * n
        self.top1 = -1
        self.top2 = len(self.items)
        
    def push1(self, item):
        if self.top1<self.top2:
            self.top1 +=1
            self.items[self.top1]= item
        else:
            return "stack overflow"
    
    def push2(self, item):
        if self.top1<self.top2:
            self.top2 -=1
            self.items[self.top2]= item
        else:
            return "stack overflow"

    def pop1(self):
        if self.top1<0:
            return "stack1 is empty"
        else:
            item = self.items[self.top1]
            self.top1 -=1
            return item
    
    def pop2(self):
        if self.top2>self.size:
            return "stack1 is empty"
        else:
            item = self.items[self.top2]
            self.top2 +=1
            return item
        
    def printStack(self):
        print(self.items)
        
ts = twoStack(10)
ts.push1(1)
ts.push2(10)
ts.push1(2)
ts.push2(9)
ts.printStack()

ts.push1(3)
ts.push2(8)
ts.push1(4)
ts.push2(7)
ts.push1(5)


ts.push2(6)
ts.push1(0)
ts.push2(0)
ts.push1(0)
ts.push2(0)
ts.printStack()
#find the middle element of a stack




