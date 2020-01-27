#This program computes the sum of the only eleven primes that are both truncatable from left to right and from right to left.

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

def istruncatable(n):
	m = str(n)
	test = True
	for i in range(0,len(m)):
		if int(m[i:]) not in primes: test = False
		if int(m[:len(m)-i]) not in primes: test = False
	return test

sum = 0
count = 0
for n in primes[4:]:
	if count == 11: break
	if str(n)[0] in {'2','3','5','7'} and str(n)[-1] in {'2','3','5','7'}:
		if istruncatable(n):
			sum += n
			count += 1

print sum
