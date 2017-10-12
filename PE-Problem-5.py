#This program determines the smallest integer which is evenly divisible by every integer from 1 to 20

import fractions

n = 1
for i in range(2,21):
	if n%i != 0:
		n*=i/fractions.gcd(n,i)
print n
