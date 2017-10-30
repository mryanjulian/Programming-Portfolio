#This program computes a list of primes up to size n via Eratosthenes number sieve.

n = 2000000
f = open("primes.txt",'w')
testlist = range(1,n)
checklist = list(1 for i in range(1,n+1))
checklist[0] = 0
for i in range(1,n):
	if checklist[i] == 1:
		k = 2
		while (i+1)*k-1<n:
			checklist[(i+1)*k-1] = 0
			k+=1
for i in range(1,n):
	if checklist[i] == 1:
		f.write(str(testlist[i])+'\n')
f.close()
