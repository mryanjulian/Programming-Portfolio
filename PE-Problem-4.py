#This program determines the largest palindrome that can be expressed as the product of two 3 digit numbers.

def reverse(n): #This function reverses the digits of the number n
	reverse = 0
	while n>0:
		reverse = 10*reverse + n%10
		n = (n-n%10)/10
	return reverse

def palindrome(n): #This function tests whether n is a palindrome
	return n == reverse(n)

largestpalindrome = 0
for a in range(100,1000):
	for b in range(a,1000):
		n = a*b
		if n>largestpalindrome and palindrome(n):
			largestpalindrome = n
print largestpalindrome
