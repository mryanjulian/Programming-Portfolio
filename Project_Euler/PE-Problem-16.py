#This program determines the sum of the digits of the number 2^1000.

n = 2**1000
sum = 0
while n>0:
	sum+=n%10
	n = (n-n%10)/10

print sum
