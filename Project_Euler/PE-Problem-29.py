#This program computes the number of distinct values of a^b with 2 <= a <=100 and 2 <= b <= 100.

#Note that the values are small enough here that even a brute force solution runs fairly quickly.
values = []
for a in range(2,101):
	for b in range(2,101):
		n = a**b
		if not n in values:
			values.append(n)

print len(values)
