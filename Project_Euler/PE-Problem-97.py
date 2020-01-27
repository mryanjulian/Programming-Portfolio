#This program finds the last ten digits of the 2357207 digit prime number 28433*2^7830457+1

n = 1
for i in range(1,7830458):
	n = n*2%10000000000
n = n*28433%10000000000+1

print n
