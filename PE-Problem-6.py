#This program computes the difference between the square of the sum of the first n natural numbers and the sum of the squares of the first n natural numbers.

n = 100
difference = 0
for a in range(1,n+1):
	for b in range(a+1,n+1):
		difference += a*b
print 2*difference
