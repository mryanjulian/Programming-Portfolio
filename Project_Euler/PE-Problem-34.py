#This program computes the sum of all numbers that are equal to the sum of the factorials of their digits.

import math

def digitfactorial(n):
	digits = list(str(n))
	factorialsum = 0
	for digit in digits:
		factorialsum+=math.factorial(int(digit))
	return factorialsum

total = 0
for n in range(3,500000):
	if n == digitfactorial(n):
		total += n

print total
