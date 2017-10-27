#This program computes the number of ways of making 2 pounds in change using 1p, 2p, 5p, 10p, 20p, 50p, 100p, and 200p coins.

value = {0:1,1:2,2:5,3:10,4:20,5:50,6:100,7:200}
memo = [[0]*401]*8
memo[0] = [1]*201+[0]*200
for i in range(1,8):
	for j in range(0,201):
		memo[i][j] = memo[i-1][j]+memo[i][j-value[i]] #Making change for j pence with the first i types of coin involves either using the first i-1 types of coin to make j pence, or using the first i types of coin to make j-value[i] pence and then adding a single coin of type i

print memo[7][200]
