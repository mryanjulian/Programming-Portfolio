#This program computes the sum of the name scores of the names in the file PE-22-names.txt

#Name scores are computed by multiplying the rank (in alphabetic order) of each name by the sum of the positions of its letters in the alphabet

f = open("PE-22-names.txt")
names = [name.strip('"') for name in f.readline().split(',')]
f.close()
names.sort()

def namesum(name):
	total = 0
	for i in range(0,len(name)):
		total += ord(name[i])-64
	return total

namescores = 0
for i in range(0,len(names)):
	namescores += (i+1)*namesum(names[i])

print namescores
