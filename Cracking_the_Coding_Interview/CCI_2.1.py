import sys
import LinkedList

root = LinkedList.Node(sys.argv[1])
for i in range(2,len(sys.argv)):
    root.append(sys.argv[i])

current = root
while current:
    print current.value
    current = current.next
print ""

def removedups(root):
    vals = set()
    current = root
    previous = None
    while current:
        if current.value in vals:
            previous.next = current.next
        else:
            vals.add(current.value)
            previous = current
        current = current.next
    return root

removedups(root)
current = root
while current:
    print current.value
    current = current.next

