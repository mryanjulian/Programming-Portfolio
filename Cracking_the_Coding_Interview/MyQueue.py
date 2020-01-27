# CCI_3.4
import Stack
class MyQueue(object):
    def __init__(self):
        self.s1 = Stack.Stack()
        self.s2 = Stack.Stack()
    def enqueue(self,item):
        self.s1.push(item)
    def dequeue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()
    def peek(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()
