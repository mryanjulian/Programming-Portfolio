#This program computes the number n <= 1000000 for which n/phi(n) is maximal, where phi(n) is Euler's phi function, i.e. the number of integers in [1..n] that are relatively prime to n.

#In this solution, we use the fact that phi(n) = n*prod_{p|n}(1-1/p), so n/phi(n) = prod_{p|n}(p/(p-1)).  From this, we can see that this value is maximized when n has a lot of small prime factors, so we can simply multiply the smallest prime numbers together until we get the largest product smaller than 1000000

f = open("primes.txt")
primes = f.readlines()
f.close()

prod = 1
i = 0
while int(primes[i])*prod<1000000:
	prod*=int(primes[i])
	i+=1

print prod
