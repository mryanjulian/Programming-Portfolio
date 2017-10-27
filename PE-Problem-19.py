#This program counts the number of Sundays that fell on the first of the month during the twentieth century (Jan 1 1901 to Dec 31 2000

weekday = 2 #Jan 1 1901 was a Tuesday
monthlength = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
count = 0

for year in range(1,101):
	for month in range(0,12):
		increment = monthlength[month]
		if month == 1 and year%4 == 0 and not year%400 == 0: increment+=1
		weekday = (weekday+monthlength[month])%7
		if weekday == 0: count+=1

print count
