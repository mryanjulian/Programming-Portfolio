# We assume that upper and lowercase letters are treated as distinct in forming palindromes.

import sys

str1 = sys.argv[1]

def isPermPal(s):
    counts = [0]*128
    for i in range(len(s)):
        if s[i] != ' ':
            counts[ord(s[i])] = (counts[ord(s[i])]+1)%2
    return (sum(counts)==0 or sum(counts)==1)

print isPermPal(str1)