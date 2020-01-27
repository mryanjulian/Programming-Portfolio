#This problem computes the product d_1*d_10*d_100*d_1000*d_10000*d_100000*d_1000000, where d_n represents the nth digit of the decimal expansion formed by concatenating the positive integers to the right of the decimal point; i.e. 0.1234567891011...

prod = 1
tarpos = 1
currpos = 1
n = 1
while tarpos < 1000001:
	if tarpos < currpos+len(str(n)):
		prod *= int(str(n)[currpos-tarpos])
		tarpos *= 10
	currpos += len(str(n))
	n += 1

print prod
