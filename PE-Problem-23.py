#This problem finds the sum of all positive integers that cannot be written as the sum of two abundant numbers, where abundant numbers have the property that the sum of their proper divisors is larger than the original number.

#Construct a list of abundant numbers:
abundant = []
for i in range(2,28124):
	divisorsum = 0
	for j in range(1,i/2+1):
		if i%j == 0:
			divisorsum += j
	if divisorsum > i:
		abundant.append(i)

abundantsum = [0]*28124
for i in range(0,len(abundant)):
	for j in range(0,len(abundant)):
		if abundant[i]+abundant[j]<28124: abundantsum[abundant[i]+abundant[j]] = 1

total = 0
for i in range(0,28124):
	if abundantsum[i] == 0:
		total += i

print total
