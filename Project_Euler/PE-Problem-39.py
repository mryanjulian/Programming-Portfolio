#This program determines the value p <= 1000 with the largest number of pythagorean triples with a+b+c = p.

def triplecount(p):
	count = 0
	for a in range(1,p-1):
		for b in range(a,p-a):
			c = p-a-b
			if a**2+b**2 == c**2: count += 1
	return count

maxp = 1
maxcount = 0
for p in range(1,1001):
	count = triplecount(p)
	if count > maxcount:
		maxp = p
		maxcount = count

print maxp
