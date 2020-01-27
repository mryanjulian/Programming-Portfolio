import sys
import LinkedList

n1 = [int(i) for i in sys.argv[1].split()]
n2 = [int(i) for i in sys.argv[2].split()]

root1 = LinkedList.Node(n1[0])
for i in range(1,len(n1)):
    root1.append(n1[i])
root2 = LinkedList.Node(n2[0])
for i in range(1,len(n2)):
    root2.append(n2[i])

def prll(root):
    curr = root
    ll = ''
    while curr:
        ll = ll + str(curr.value) +', '
        curr = curr.next
    print ll

prll(root1)
prll(root2)

def addll(root1,root2):
    curr1 = root1
    curr2 = root2
    total = LinkedList.Node(None)
    carry = 0
    while curr1 or curr2:
        if not curr1:
            total.append(curr2.value+carry)
            carry = 0
            curr2 = curr2.next
        elif not curr2:
            total.append(curr1.value+carry)
            carry = 0
            curr1 = curr1.next
        else:
            total.append((curr1.value+curr2.value+carry)%10)
            if curr1.value+curr2.value+carry >= 10:
                carry = 1
            else:
                carry = 0
            curr1 = curr1.next
            curr2 = curr2.next
    return total.next

total = addll(root1,root2)
prll(total)
