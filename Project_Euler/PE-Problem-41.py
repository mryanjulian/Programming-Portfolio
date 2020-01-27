#This problem computes the largest n-digit pandigital prime.

#We note that this number must have 7 digits, so we use our prime list that contains up to the 7 digit primes.

f = open('primesto10000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

max = 1
for prime in primes:
	n = len(str(prime))
	if set(str(prime)) == set(''.join([str(k) for k in range(1,n+1)])):
		if prime > max: max = prime

print max
