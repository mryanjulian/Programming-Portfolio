#This program determines the denominator d < 1000 with the longest repetend in the fraction 1/d

#This computes repetend lengths for natural numbers n that are relatively prime to 10
def repetendlength(n):
	length = 1
	r = 10%n
	while r != 0 and r != 1:
		r = (10*r)%n
		length += 1
	return length

maxn = 1
maxrepetend = 1
for i in range(1,1001):
	if i%2 != 0 and i%5 != 0:
		repetend = repetendlength(i)
		if repetend > maxrepetend:
			maxn = i
			maxrepetend = repetend

print maxn
