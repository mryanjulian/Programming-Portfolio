#This program computes the index of the first 1000-digit Fibonacci number (where the indexing starts with f_1 = f_2 = 1)

a = 1
b = 1
c = 2
index = 3
while len(str(c))<1000:
	index+=1
	a = b
	b = c
	c = a+b

print index
