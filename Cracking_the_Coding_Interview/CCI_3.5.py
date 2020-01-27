import sys
import Stack

stack = Stack.Stack()
for i in range(1,len(sys.argv)):
    stack.push(int(sys.argv[i]))

def sortstack(stack):
    stack2 = Stack.Stack()
    while not stack.isEmpty():
        item = stack.pop()
        if stack2.isEmpty() or item >= stack2.peek():
            stack2.push(item)
        else:
            while not stack2.isEmpty() and stack2.peek() > item:
                stack.push(stack2.pop())
            stack2.push(item)
    while not stack2.isEmpty():
        stack.push(stack2.pop())
    return stack

print stack.data
stack = sortstack(stack)
print stack.data