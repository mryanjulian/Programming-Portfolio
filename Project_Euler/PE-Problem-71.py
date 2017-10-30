#This program computes the numerator of the largest reduced fraction n/d<3/7 with d<=1000000.

def gcd(a,b):
	r = b
	while r>0:
		q = a/b
		tempr = a-b*q
		if tempr == 0: return r
		else: r = tempr
		a = b
		b = r

truenum = 1
truedenom = 3
denom = 11
while denom<1000000:
	denom += 1
	num = int(3*denom/7)-1
	if gcd(num,denom) == 1 and truenum*denom<num*truedenom:
		truenum = num
		truedenom = denom

print truenum
