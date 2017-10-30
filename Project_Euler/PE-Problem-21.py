#This program computes the sum of all amicable numbers under 10000.
#a and b are amicable if d(a) = b and d(b) = a, where d(n) is the sum of the proper divisors of n.

def divisorsum(n):
	total = 1
	for i in range(2,int(n**.5)):
		if n%i == 0: total+=i+n/i
	return total

amicablesum = 0
amicablechecks = [0]*10000
for a in range(1,10000):
	if amicablechecks[a] == 0:
		b = divisorsum(a)
		if b<10000: amicablechecks[b] = 1
		amicablechecks[a] = 1
		if a != b and divisorsum(b) == a: amicablesum+=a+b

print amicablesum
