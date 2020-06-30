import sys
DEBUG=True
#DEBUG=False
if DEBUG:
    f=open("202006_5th/D_input.txt")
else:
    f=sys.stdin
ans=1
n=int(f.readline().strip())
prime=[]
# Start from where n is equal to 2
for _ in range(1,n):
    number_of_multiply=[]
    tmp=_+1
    num_of_divisor=1
    for __ in prime:
        cnt=0
        if tmp==1:
            break
        while (tmp%__)==0:
            cnt+=1;tmp//=__;
        if cnt>0:
            num_of_divisor*=cnt+1
    if num_of_divisor==1:
        prime.append(_+1)
        ans+=(_+1)*2
    else:
        ans+=(_+1)*num_of_divisor
print(ans)