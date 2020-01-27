import sys
import LinkedList

root = LinkedList.Node(sys.argv[1])
for i in range(2,len(sys.argv)):
    root.append(sys.argv[i])

def prll(root):
    curr = root
    ll = ''
    while curr:
        ll = ll + str(curr.value) +', '
        curr = curr.next
    print ll

prll(root)

def isPalindrome(root):
    curr = root
    revcurr = LinkedList.Node(curr.value)
    while curr:
        curr = curr.next
        if curr:
            revnew = LinkedList.Node(curr.value)
            revnew.next = revcurr
            revcurr = revnew
    prll(revcurr)
    curr = root
    curr2 = revcurr
    while curr:
        if curr.value != revcurr.value:
            return False
        curr = curr.next
        revcurr = revcurr.next
    return True

print(isPalindrome(root))