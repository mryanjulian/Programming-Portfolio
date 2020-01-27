#This problem computes the last 10 digits of the sum 1^1+2^2+...+1000^1000.

sum = 0
for n in range(1,1000):
	sum = (sum+n**n)%10000000000

print sum
