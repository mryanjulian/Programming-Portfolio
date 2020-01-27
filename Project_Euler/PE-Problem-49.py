#This problem computes the two arithmetic sequences of three 4-digit primes with the property that each of the three prime numbers are permutations of one another.

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

#Note that the first 4-digit prime is the 168th prime, and the last one is the 1228th prime
fdprimes = primes[168:1228]

for i in range(1,len(fdprimes)):
	for j in range(len(fdprimes)-1,i,-1):
		pi = fdprimes[i]
		pj = fdprimes[j]
		if set(str(pi)) == set(str(pj)):
			ave = (pi+pj)/2
			if set(str(ave)) == set(str(pi)) and ave in fdprimes:
				print pi,ave,pj
