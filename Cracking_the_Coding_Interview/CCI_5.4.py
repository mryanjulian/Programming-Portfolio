import sys

n = sys.argv[1]

def getNext(n):
    n = list('0'+n)
    pos = len(n)-1
    numones = 0
    while n[pos] == '0':
        pos -= 1
    while n[pos] == '1':
        pos -= 1
        numones += 1
    n[pos] = '1'
    for i in range(pos+1,len(n)-numones+1):
        n[i] = '0'
    for i in range(len(n)-numones+1,len(n)):
        n[i] = '1'
    if n[0] == '0': n = n[1:]
    return ''.join(n)

def getPrev(n):
    n = list('0'+n)
    pos = len(n)-1
    numones = 0
    while n[pos] == '1':
        pos -= 1
        numones += 1
    if pos == 0: return 'Error: Smallest such number'
    while n[pos] == '0':
        pos -= 1
    n[pos] = '0'
    for i in range(pos+1,pos+2+numones):
        n[i] = '1'
    for i in range(pos+2+numones,len(n)):
        n[i] = '0'
    if n[0] == '0': n = n[1:]
    return ''.join(n)

print 'larger:', getNext(n)
print 'smaller:', getPrev(n)