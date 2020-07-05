import sys
from math import comb
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("202006_5th/E_input.txt")
else:
    f=sys.stdin
N,M=map(int,f.readline().split())
mod=(10**9)+7
print((comb(M,N)**2*N)%mod)
f.close()