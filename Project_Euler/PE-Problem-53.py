#This program computes the number of binomial coefficients, binom(n,k), larger than 1000000 with n<=100.

count = 0
binom = [[0 for i in range(0,102)] for j in range(0,101)]
binom[0][0] = 1

for n in range(1,101):
	for k in range(0,n+2):
		binom[n][k]=binom[n-1][k-1]+binom[n-1][k]
		if binom[n][k] > 1000000: count+=1

print count
