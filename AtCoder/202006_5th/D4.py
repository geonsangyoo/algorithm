import sys
DEBUG=True
#DEBUG=False
if DEBUG:
    f=open("202006_5th/D_input.txt")
else:
    f=sys.stdin
def get_dividor(num):
    ans=0
    for _ in range(1,num+1):
        if _**2>num:
            break
        if num%_==0:
            ans+=1
            if (_**2)!=num:
                ans+=1
    return ans
n=int(f.readline().strip())
ans_sum=0
for _ in range(1,n+1):
    ans_sum+=_*get_dividor(_)
print(ans_sum)