#This program returns the value of the nth prime.
#Note that the program primelist.py was used to compute a list of primes in the file primes.txt

n = 10001
f = open("primes.txt")
primes = f.readlines()
print int(primes[n-1])
f.close()
