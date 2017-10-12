#There exists a unique pythagorean triple such that a^2 + b^2 = c^2 and a + b + c = 1000
#This program computes this triple and prints the product abc

for a in range(1,1001):
	asquared = a**2
	for b in range(a+1,1001):
		bsquared = b**2
		c = 1000-a-b
		if c>b and asquared+bsquared == c**2:
			print a*b*c
			break
