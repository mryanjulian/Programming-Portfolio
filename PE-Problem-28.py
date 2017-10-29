#This program computes the sum of the numbers on the diagonals in a 1001 by 1001 number spiral.

#This solution results from first computing by hand a quadratic representing the sum of the four corners of an i by i number spiral, which is equivalent to 4 times the number in the center of the left edge of that square.
print sum([4*(4*i*i+i+1) for i in range(0,501)])-3

