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
for _ in range(N):
    A=(_+1)*2
    I=int(math.sqrt(A))
    cnt=0
    for __ in range(I):
        A2=A-((__+1)**2)
        if A2<=0:
            break
        I2=int(math.sqrt(A2))
        for ___ in range(I2):
            A3=A2-((___+1)**2)
            if A3<=0:
                break
            I3=int(math.sqrt(A3))
            for ____ in range(I3):
                if ((__+___+2)**2)+((___+____+2)**2)+((__+____+2)**2)==A:
                    cnt+=1
                    break
    print(cnt)
f.close()