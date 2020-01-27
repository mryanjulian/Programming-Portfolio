import sys

n = int(sys.argv[1],2)

def swap(n):
    return ((n&0xAAAAAAAA)>>1)|((n&0x55555555)<<1)

print bin(swap(n))