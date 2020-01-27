#This program computes the number of number chains formed by iterating a function that sums the squares of the digits of each number that end at the value 89.

#Note that any such number chain eventually arrives at 1 or 89.

def chain(n):
	next = 0
	for i in range(0,len(str(n))):
		next += (n%10)**2
		n = n/10
	return next

test = {1:1,89:89}
count = 0
for n in range(1,10000000):
	val = n
	while not val in test:
		val = chain(val)
	test[n] = test[val]
	if test[n] == 89: count += 1

print count
