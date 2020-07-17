import sys
DEBUG=True
# DEBUG=False
if DEBUG:
    f=open("202007_2nd/A_input.txt")
else:
    f=sys.stdin
l,h,d=map(int,f.readline().split())
ans=0
for _ in range(l,h+1):
    ans=ans+1 if _%d==0 else ans
print(ans)