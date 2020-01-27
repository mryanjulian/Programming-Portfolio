#This problem computes the second smallest number that is a triangular number, a pentagonal number, and a hexagonal number.

#Note that every hexagonal number is also a triangular number.

hex = 1
hexinc = 5
for n in range(0,100000):
	hex += hexinc
	hexinc += 4
	penttest = ((24*hex+1)**(1./2)+1)/6
	if int(penttest) == penttest and hex > 40755:
		print hex
		exit()
