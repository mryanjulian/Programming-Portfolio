import sys
import LinkedList

list1 = sys.argv[1].split()
root1 = LinkedList.Node(list1[0])
for i in range(1,len(list1)):
    root1.append(list1[i])
list2 = sys.argv[2].split()
root2 = LinkedList.Node(list2[0])
for i in range(1,len(list2)):
    root2.append(list2[i])

def prll(root):
    curr = root
    ll = ''
    while curr:
        ll = ll + str(curr.value) +', '
        curr = curr.next
    print ll

def intersect(root1,root2):
    l1, fin1 = length(root1)
    l2, fin2 = length(root2)
    if fin1 == fin2:
        if l1 >= l2:
            coll = intpt(root1,root2,l1-l2)
        else:
            coll = intpt(root2,root1,l2-l1)
    else: return False
    return coll

root1.next.next.next.next = root2.next.next #Creates an intersection for testing

def length(root):
    curr = root
    length = 1
    while curr.next:
        length += 1
        curr = curr.next
    return length, curr

def intpt(root1,root2,d):
    curr1 = root1
    curr2 = root2
    for i in range(d):
        curr1 = curr1.next
    while curr1 != curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1

prll(root1)
prll(root2)
coll = intersect(root1,root2)
print coll
if coll: print coll.value