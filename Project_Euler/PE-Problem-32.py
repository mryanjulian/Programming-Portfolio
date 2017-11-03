#This program computes the sum of all products whose multiplicand/multiplier/product identity can be written using each digit 1-9.

def ispandigital(a,b):
	c = a*b
	return len(set(str(a)+str(b)+str(c))) == 9 and len(str(a)+str(b)+str(c)) == 9 and not '0' in set(str(a)+str(b)+str(c))

pandigitalset = set([])
for a in range(2,100):
	for b in range(10**(4-len(str(a))),10000):
		if ispandigital(a,b):
			pandigitalset.add(a*b)

total = 0
for element in pandigitalset:
	total+=element
print total
