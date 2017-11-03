#This program computes the number of circular primes (where every rotation of the digits produces another prime) below 1000000.

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

def iscircular(n):
	length = len(str(n))
	for i in range(0,length):
		n = int(str(n)[1:length]+str(n)[0])
		if not n in primes: return False
	return True

count = 2 #This counts the primes 2 and 5 which will be excluded below
for prime in primes:
	if set(str(prime)).issubset({'1','3','7','9'}):
		if iscircular(prime):
			count += 1

print count
