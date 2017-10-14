#This problem computes the first 10 digits of the sum of the 100 50-digit numbers in the file PE-13-numbers.txt

f = open("PE-13-numbers.txt")
numbers = f.readlines()
f.close()

total = 0
for i in range(0,len(numbers)):
	total+=int(numbers[i][0:11])

print str(total)[0:10]
