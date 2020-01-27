#This problem computes the first four consecutive integers to have 4 distinct prime factors each.  The output is the smallest of these numbers.

import math

f = open('primesto1000000.txt')
primes = [int(prime) for prime in f.readlines()]
f.close()

top = 200000
fourfacs = [0 for n in range(0,top)]
def fillfacs(a,b,c,d):
	for w in range(1,int(math.log(top/(b*c*d)+1,a))+1):
		for x in range(1,int(math.log(top/(a*c*d)+1,b))+1):
			for y in range(1,int(math.log(top/(a*b*d)+1,c))+1):
				for z in range(1,int(math.log(top/(a*b*c)+1,d))+1):
					if a**w*b**x*c**y*d**z < top:
						fourfacs[a**w*b**x*c**y*d**z] = 1
	return

for a in primes[0:10]:
	for b in primes [0:10]:
		if not a == b:
			for c in primes[0:20]:
				if not a == c and not b == c:
					for d in primes[0:200]:
						if not a == d and not b == d and not c == d:
							fillfacs(a,b,c,d)

for n in range(1,top):
	if fourfacs[n] == 1:
		if fourfacs[n+1] == 1:
			if fourfacs[n+2] == 1:
				if fourfacs[n+3] == 1:
					print n
					break
