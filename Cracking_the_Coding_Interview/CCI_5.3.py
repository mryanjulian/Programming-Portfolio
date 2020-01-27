# In this problem, I assume that a binary string of all 1's can still
# have a preceding 0 bit flipped to form a longer chain of 1's.
import sys

n = sys.argv[1]

def flipBit(n):
    prevlen = 0
    currlen = 0
    longest = 0
    prev = '0'
    for pos in range(0,len(n)):
        if n[pos] == '1':
            prev = '1'
            currlen += 1
            if currlen + prevlen + 1 > longest: longest = currlen + prevlen + 1
        elif n[pos] == '0' and prev == '0':
            prevlen = 0
            currlen = 0
        else:
            prev = '0'
            prevlen = currlen
            currlen = 0
    return longest

print flipBit(n)
