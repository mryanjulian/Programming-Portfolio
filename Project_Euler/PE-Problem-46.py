#This problem computes the smallest odd composite number that cannot be written as the sum of a prime and twice a square, disproving a conjecture of Goldbach.

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

odds = [0 for n in range(0,10000)]
for i in range(0,int(20001**(1./2))+1):
	dsqr = 2*i**2
	for j in range(1,len(primes)):
		if (dsqr+primes[j])/2+1 > 9999: break
		odds[((dsqr+primes[j])-1)/2] = 1
for n in range(1,10000):
	if odds[n] == 0:
		print 2*n+1
		exit()
