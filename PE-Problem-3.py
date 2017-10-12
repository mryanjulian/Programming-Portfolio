#This program determines the largest prime factor of the number 600851475143

n = 600851475143
f = open("primes.txt")
primes = f.readlines()
for p in primes:
	if n%int(p) == 0:
		maxprime = int(p)
print maxprime
