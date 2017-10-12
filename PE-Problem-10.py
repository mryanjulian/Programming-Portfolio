#This program computes the sum of the first 2000000 primes stored in the file primes2.txt

f = open("primes.txt")
primes = f.readlines()
total = 0
for prime in primes:
	if int(prime)<2000000:
		total+=int(prime)
print total
