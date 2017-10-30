#This program counts the number of lattice paths from the top left to the bottom right of a 20 x 20 grid, taking only steps down or right.

#There is a fairly obvious combinatorial solution to this problem, so this problem just computes 40 choose 20 with the binomial coefficient function in scipy.

import scipy.special
print scipy.special.comb(40,20,exact = True)
