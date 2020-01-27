import sys

str1 = sys.argv[1]
truelen = int(sys.argv[2])

def URLify(si,l):
    s = list(si)
    count = 0
    for i in range(l):
        if s[i] == ' ':
            count += 1
    j = l + 2*count
    for i in range(l-1,0,-1):
        if s[i] == ' ':
            s[j-1] = '0'
            s[j-2] = '2'
            s[j-3] = '%'
            j = j-3
        else:
            s[j-1] = s[i]
            j -= 1
    return ''.join(s)

print URLify(str1,truelen)