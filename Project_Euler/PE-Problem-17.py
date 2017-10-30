#This program determines the number of letters necessary to write out all the numbers from 1 to 1000 (inclusive).

#This function returns the letter count for small numbers n<=1000
def lettercount(n):
	if n == 0: return 0
	if n in [1,2,6,10]: return 3
	if n in [4,5,9]: return 4
	if n in [3,7,8,40,50,60]: return 5
	if n in [11,12,20,30,80,90]: return 6
	if n in [15,16,70]: return 7
	if n in [13,14,18,19]: return 8
	if n in [17]: return 9
	if n in range(21,100) and not n in [30,40,50,60,70,80,90]: return lettercount(n%10)+lettercount(n-n%10)
	if n in range(100,1000):
		count = 10+lettercount(n%100)+lettercount((n-n%100)/100)
		if n%100 == 0: count-=3
		return count
	if n == 1000: return 11

total = 0
for n in range(1,1001):
	total+=lettercount(n)

print total
