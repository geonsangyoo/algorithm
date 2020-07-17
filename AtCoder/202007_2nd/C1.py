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
ans=[0 for _ in range(N)]
for _ in range(N):
    A=(_+1)*2
    I=int(math.sqrt(A/3))
    cnt=0
    for __ in range(I):
        I2=I-__
        for ___ in range(I2):
            I3=I2-___
            for ____ in range(I3):
                if ((__+___+2)**2)+((___+____+2)**2)+((__+____+2)**2)==A:
                    cnt+=1
    ans[_]=cnt
for _ in range(N):
    print(ans[_])
f.close()