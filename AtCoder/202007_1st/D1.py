import sys
DEBUG=True
# DEBUG=False
if DEBUG:
    f=open("202007_1st/D_input.txt")
else:
    f=sys.stdin
N=int(f.readline().strip())
A=list(map(int,f.readline().split()))
A.sort(reverse=True)
ans=0
for _ in range(1,N):
    ans+=A[int(_/2)]
print(ans)
f.close()