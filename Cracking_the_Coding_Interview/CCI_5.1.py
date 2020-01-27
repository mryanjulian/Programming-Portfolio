n = 0b10000000000
m = 0b10011
i = 2
j = 6

def insert(n,m,i,j):
    mask = ~((2**(j-i+1)-1)<<i)
    return bin((n & mask) | (m << i))

print insert(n,m,i,j)