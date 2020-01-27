#This problem computes the pair of pentagonal numbers P_j and P_k for which their sum and difference are pentagonal with the smallest difference |P_k-P_j|.  The output is the difference between P_j and P_k.

pentagonals = [1]
increment = 4
for j in range(0,10001):
	pj = pentagonals[j]
	pentagonals.append(pj+increment)
	increment += 3
	for k in range(0,j):
		pk = pentagonals[k]
		sum = pj+pk
		test = ((24*sum+1)**(1./2)+1)/6
		if int(test) == test:
			diff = pj-pk
			test =  ((24*diff+1)**(1./2)+1)/6
			if int(test) == test:
				print diff
				exit()
