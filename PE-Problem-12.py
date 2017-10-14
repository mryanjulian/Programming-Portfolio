#This program computes the first triangular number with over 500 divisors

#This function counts the number of divisors of a number n
def divcount(n):
	count = 0
	for i in range(1,n+1):
		if n%i == 0:
			count+=1
	return count

#This searches for the first triangular number with over 500 divisors
divisors = 0
n = 1
divmax = 1
while divmax<500:
	n += 1
	if n%2 == 0:
		divisors = divcount(n/2)*divcount(n+1)
	else:
		divisors = divcount(n)*divcount((n+1)/2)
	if divisors>divmax:
		divmax = divisors

print n*(n+1)/2
