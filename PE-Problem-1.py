#This program computes the sum of all the multiples of 3 or 5 below 1000

s = 0
for i in range(1,334):
	s += 3*i
for i in range(1,200):
	s += 5*i
for i in range(1,67):
	s -= 15*i
print s
