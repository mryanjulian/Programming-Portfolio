#This program finds the sum of P(i,4^i) as i ranges from 1 to 31.
#P(s,N) is defined to be the number of integers n, 1<n<N, s.t. streak(n) = s
#streak(n) is defined to be the smallest integer k such that n+k is not divisible by k+1

def streak(n):
	k = 1
	while (n+k)%(k+1) == 0:
		k += 1
	return k

#def P(s,N):
#	count = 0
#	for n in range(2,N):
#		if streak(n) == s: count+=1
#	return count
#
#total = 0
#for i in range(1,31):
#	print (i,P(i,4**i))
#	total += P(i,4**i)
#
#print total
