import sys
import LinkedList

k = int(sys.argv[1])
root = LinkedList.Node(sys.argv[2])
for i in range(3,len(sys.argv)):
    root.append(sys.argv[i])

def kfromlast(root,k):
    l = root
    r = root
    for i in range(1,k):
        if r.next:
            r = r.next
        else:
            print "k is too large"
            return
    while r.next:
        l = l.next
        r = r.next
    return l.value

print(kfromlast(root,k))