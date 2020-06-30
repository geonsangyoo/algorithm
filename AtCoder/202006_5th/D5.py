import sys
DEBUG=True
#DEBUG=False
if DEBUG:
    f=open("202006_5th/D_input.txt")
else:
    f=sys.stdin
ans_sum=0
n=int(f.readline().strip())
for _ in range(1,n+1):
    num=n//_
    ans_sum+=_*((num*(num+1))//2)
print(ans_sum)