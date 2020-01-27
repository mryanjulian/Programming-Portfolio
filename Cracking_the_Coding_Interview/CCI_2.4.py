import sys
import LinkedList

k = int(sys.argv[1])
root = LinkedList.Node(int(sys.argv[2]))
for i in range(3,len(sys.argv)):
    root.append(int(sys.argv[i]))

def prll(root):
    curr = root
    ll = ''
    while curr:
        ll = ll + str(curr.value) +', '
        curr = curr.next
    print ll

def partition(root):
    curr = root
    marker = LinkedList.Node('*')
    left = marker
    right = marker
    while curr:
        if curr.value < k:
            nex = curr.next
            curr.next = left
            left = curr
            curr = nex
        elif curr.value >= k:
            nex = curr.next
            curr.next = None
            right.next = curr
            right = curr
            curr = nex
    marker.value = marker.next.value
    marker.next = marker.next.next
    return left

prll(root)

root = partition(root)

prll(root)