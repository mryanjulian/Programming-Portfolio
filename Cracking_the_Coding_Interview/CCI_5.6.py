import sys

a = int(sys.argv[1],2)
b = int(sys.argv[2],2)

def hamming(a,b):
    c = a ^ b
    count = 0
    while c != 0:
        count += 1
        c = c&(c-1)
    return count

print hamming(a,b)