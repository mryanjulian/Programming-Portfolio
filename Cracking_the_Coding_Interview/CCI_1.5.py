import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

def dist1(s1,s2):
    if len(s1) == len(s2):
        return replace(s1,s2)
    elif len(s1) == len(s2)+1:
        return delete(s1,s2)
    elif len(s1)+1 == len(s2):
        return delete(s2,s1)
    else:
        return False

def replace(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1: return False
    return True

def delete(s1,s2):
    d = 0
    for i in range(len(s2)):
        if s1[i+d] != s2[i]:
            d += 1
            if d > 1: return False
    return True

print dist1(str1,str2)