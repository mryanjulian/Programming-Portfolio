import sys

str1 = sys.argv[1]

def uniqueTest(s):
    tests = [0]*128
    for i in range(len(s)):
        pos = ord(s[i])
        if tests[pos] == 1:
            return False
        else:
            tests[pos] = 1
    return True

print uniqueTest(str1)