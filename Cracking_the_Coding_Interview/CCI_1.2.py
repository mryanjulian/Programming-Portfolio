import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

def perms(s1,s2):
    counts = [0]*128
    if len(str1) != len(str2):
        return False
    l = len(s1)
    for i in range(l):
        counts[ord(s1[i])] += 1
        counts[ord(s2[i])] -= 1
    test = True
    for i in range(128):
        if counts[i] != 0:
            test = False
    return test

print perms(str1,str2)