import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("202006_5th/C_input.txt")
else:
    f=sys.stdin
#----
M,N,K=map(int,f.readline().split())
ans=0
__=N
M_shelf=list(map(int,f.readline().split()))
N_shelf=list(map(int,f.readline().split()))
M_partial=[]
N_partial=[]
M_partial.append(0)
N_partial.append(0)
#----
for _ in range(M):
    M_partial.append(M_partial[_]+M_shelf[_])
for _ in range(N):
    N_partial.append(N_partial[_]+N_shelf[_])
for _ in range(M+1):
    R=K-M_partial[_]
    if R<0:
        break
    while R<N_partial[__]:
        __-=1
    ans=max(ans,_+__)
print(ans)
f.close()