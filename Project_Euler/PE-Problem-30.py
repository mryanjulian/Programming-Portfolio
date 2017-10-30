#This program computes the sum of all the numbers that can be expressed as the sum of the fifth powers of their digits.

def isdigitpowersum(n):
	powersum = 0
	for i in range(0,len(str(n))):
		powersum += int(str(n)[i])**5
	return powersum == n

total = 0
for n in range(2,1000000):
	if isdigitpowersum(n): total += n

print total
