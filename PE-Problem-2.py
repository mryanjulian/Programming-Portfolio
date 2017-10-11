#This program computes the sum of the even valued terms of the Fibonacci sequence whose values do not exceed four million.

#Note that the every third term of the standard Fibonacci sequence (given by f_n = f_(n-1) + f_(n-2) and f_1 = f_2 = 1) will be even, so we first create a recursion for these terms: f_(3n) = 4f_(3n-3) + f_(3n-6).

s = 10 #We initialize the sum with the sum of the first two even Fibonacci numbers
a = 2
b = 8
c = a+4*b
while c < 4000000:
	s += c
	a = b
	b = c
	c = a+4*b
print s
