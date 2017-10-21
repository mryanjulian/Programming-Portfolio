#This program computes the number below 1000000 that produces the longest Collatz sequence

collatz = dict()
collatz[1] = 1
countmax = 1
nmax = 1

def collatzcounter(n):
	if n in collatz: return collatz[n]
	elif n%2 == 0:
		collatz[n] = 1 + collatzcounter(n/2)
		return collatz[n]
	else:
		collatz[n] = 1 + collatzcounter(3*n+1)
		return collatz[n]

for n in range(1,1000000):
	count = collatzcounter(n)
	if count > countmax:
		countmax = count
		nmax = n

print nmax
