#This program determines the product of the coefficient, a and b, of the quadratic n^2+an+b that produces the largest number of primes for consecutive values of n, starting with n = 0, for |a|<1000 and |b|<=1000.

f = open("primes.txt")
primes = [int(prime) for prime in f.readlines()]
f.close()

primes = primes[0:5000] #Most of the delay comes from the prime check, so we limit the list of primes we're considering to just the first 5000

def numprimes(a,b):
	count = 0
	n = 0
	while n*n+a*n+b in primes:
		n += 1
		count += 1
	return count

index = 0
prime = primes[index]
primesunder1000 = []
while prime<1000:
	primesunder1000.append(prime)
	index += 1
	prime = primes[index]

maxa = 0
maxb = 0
maxprimes = 0
for b in primesunder1000[len(primesunder1000)-1:0:-1]:
	for a in range(-b,1000):
		newprimes = numprimes(a,b)
		if newprimes > maxprimes:
			maxa = a
			maxb = b
			maxprimes = newprimes

print maxa*maxb
