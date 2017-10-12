#This program computes a list of primes up to size n via Eratosthenes number sieve.

n = 200000
f = open("primes.txt",'w')
primes = [2]
f.write("2"+'\n')
testlist = range(3,n,2) #Initialize with only odd integers to avoid needless divisibility tests
i = 0
while primes[i] < testlist[len(testlist)-1]:
	for n in testlist:
		if n%primes[i]==0:
			testlist.remove(n)
	i+=1
	primes.append(testlist[0])
	f.write(str(testlist[0])+'\n')
f.close()
