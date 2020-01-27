import sys
import LinkedList

root = LinkedList.Node(sys.argv[1])
for i in range(2,len(sys.argv)):
    root.append(sys.argv[i])

current = root
while current:
    print current.value
    current = current.next

def removenode(node):
    if node == None or node.next == None:
        print "Error"
    else:
        node.value = node.next.value
        node.next = node.next.next
    return
    

node = root.next.next.next
removenode(node)

print ""
current = root
while current:
    print current.value
    current = current.next