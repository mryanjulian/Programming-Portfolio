#This problem computes the number of triangle words in the file PE-42-words.txt, where triangle words are words where the sum of the values of the letters is a triangular number.

f = open('PE-42-words.txt')
list = f.readlines()
f.close()

words = list[0].split('"')

trinums = [1]
for n in range(2,100):
	trinums.append(trinums[n-2]+n)

count = 0
for word in words:
	sum = 0
	for letter in word:
		sum += ord(letter)-64
	if sum in trinums:
		count += 1

print count
