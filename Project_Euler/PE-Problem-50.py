#This problem computes the prime number below 1000000 that can be written as the sum of the most consecutive primes.

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

p = 41
for k in range(21,545):
	sum = 0
	for n in range(0,k):
		sum += primes[n]
	start = 0
	end = k
	while end < 5000:
		if sum%2 == 1 and sum in primes:
			p = sum
			break
		sum = sum-primes[start]+primes[end]
		start += 1
		end += 1

print p
