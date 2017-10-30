#This program computes the sum of the digits of the number 100!.

import math

def digitcount(n):
	count = 0
	while n>0:
		count+=n%10
		n = (n-n%10)/10
	return count

print digitcount(math.factorial(100))
