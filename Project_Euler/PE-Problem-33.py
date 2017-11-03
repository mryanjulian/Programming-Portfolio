#This program computes the denominator of the product of all fractions which may be non-trivially and incorrectly reduced in the same way as 49/98 = 4/8

from fractions import gcd

digitlist = [str(n) for n in range(1,10)]
numerator = 1
denominator = 1
for a in digitlist:
	for b in digitlist:
		for c in digitlist:
			if a!=b and b!=c and float(a+b)/float(b+c)==float(a)/float(c):
				numerator*=int(a)
				denominator*=int(c)

print denominator/gcd(numerator,denominator)
