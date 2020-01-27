#This problem computes the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n>1.

max = 0
for i in range(2,10):
	listfac = range(1,i)
	for j in range(1,10000):
		n = ''
		for k in listfac:
			n = n + str(k*j)
		if len(n) == 9 and set(n) == {'1','2','3','4','5','6','7','8','9'}:
			if int(n) > max: max = int(n)

print max
