import sys
import LinkedList

root = LinkedList.Node(sys.argv[1])
for i in range(2,len(sys.argv)):
    root.append(sys.argv[i])

curr = root
while curr.next:
    curr = curr.next
curr.next = root.next.next.next.next #Establish a loop for testing.

def loopnode(root):
    p1 = root
    p2 = root
    collision = False
    while not collision:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            collision = True
    p2 = root
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

coll = loopnode(root)
print coll.value