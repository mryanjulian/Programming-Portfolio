import sys

string = sys.argv[1]

def compress(s):
    compressed = ''
    i = 0
    n = 0
    while i+n<len(s):
        c = s[i]
        while i+n<len(s) and s[i+n] == c:
            n += 1
        compressed = compressed + c + str(n)
        i = i+n
        n = 0
    if len(compressed)<len(s):
        return compressed
    else:
        return s

print compress(string)