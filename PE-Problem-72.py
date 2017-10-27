#This program counts the number of reduced proper fractions n/d with d<=1000000.

f = open("primes.txt")
primes = [int(prime) for prime in f.readlines()]
f.close()

def phi(n):
	i = 0
	m = n
	factors = []
	while m>1:
		if m%primes[i] == 0:
			factors.append(primes[i])
			while m%primes[i] == 0:
				m = m/primes[i]
		i+=1
	prod = n
	for prime in factors:
		prod = prod-prod/prime
	return prod

count = 0
for d in range(2,1000001):
	count += phi(d)

print count
