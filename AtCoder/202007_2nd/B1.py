import sys
DEBUG=True
# DEBUG=False
if DEBUG:
    f=open("202007_2nd/B_input.txt")
else:
    f=sys.stdin
N=int(f.readline().strip())
A=list(map(int,f.readline().split()))
ans=0
for _ in range(N):
    ans=ans+1 if (_+1)%2 and (A[_]%2) else ans
print(ans)
f.close()