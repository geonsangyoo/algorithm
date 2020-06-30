import sys
DEBUG=True
#DEBUG=False
if DEBUG:
    f=open("202006_5th/D_input.txt")
else:
    f=sys.stdin
ans=1
n=int(f.readline().strip())
dp=[0 for _ in range(n)]
prime=[]
number_of_multiply=[]
# Start from where n is equal to 2
for _ in range(1,n):
    number_of_multiply.clear()
    tmp=_+1
    for __ in prime:
        cnt=0
        #exception case1. PN^2
        if (_+1)==(__**2):
            cnt=2
            number_of_multiply.append(cnt)
            break
        while (tmp%__)==0:
            cnt+=1;tmp//=__;
        if cnt>0:
            number_of_multiply.append(cnt)
    if len(number_of_multiply)==0:
        prime.append(_+1)
        ans+=(_+1)*2
    else:
        num_of_divisor=1
        for ___ in number_of_multiply:
            num_of_divisor*=___+1
        ans+=(_+1)*num_of_divisor
print(ans)