#This problem computes the sum of all the numbers less than 1000000 that are palindromic in both base 10 and base 2.

def ispalindrome(n):
	reverse = int(str(n)[len(str(n))-1::-1])
	return reverse == n

total = 1 #This starts by including 1 as a palindrome in both bases
for i in range(1,2**11):
	for j in range(0,3):
		k = str(j)
		if j == 2: k = ''
		n = int(bin(i)[2:]+k+bin(i)[len(bin(i))-1:1:-1],base=2)
		if n<1000000 and ispalindrome(n) and bin(n)[2:] == bin(n)[len(bin(n))-1:1:-1]:
			total+=n
			print n

print total
