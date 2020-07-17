import sys,math
DEBUG=True
# DEBUG=False
if DEBUG:
    f=open("202007_2nd/C_input.txt")
else:
    f=sys.stdin
# Find the number of triples of integers (x,y,z) such that
# (x+y)**2 + (y+z)**2 + (x+z)**2 = 2*N
N=int(f.readline().strip())
# Stack values as x,y,z are counted up
ans=[0 for _ in range(N)]
I=int(math.sqrt(N))
for __ in range(I):
    A2=N-((__+1)**2)
    if A2<=0:
        break
    I2=int(math.sqrt(A2))
    for ___ in range(I2):
        A3=A2-((___+1)**2)
        if A3<=0:
            break
        I3=int(math.sqrt(A3))
        for ____ in range(I3):
            tmp=((__+___+2)**2)+((___+____+2)**2)+((__+____+2)**2)
            if tmp<=2*N:
                ans[int(tmp/2)-1]+=1
            else:
                break
for _ in range(N):
    print(ans[_])
f.close()