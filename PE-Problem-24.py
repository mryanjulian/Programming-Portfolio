#This program computes the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9.

import math

remainingperms = 999999
remainingdigits = [0,1,2,3,4,5,6,7,8,9]
millionth = ""
for i in range(9,-1,-1):
	n = math.factorial(i)
	k = remainingperms/n
	remainingperms -= k*n
	millionth += str(remainingdigits.pop(k))

print millionth
