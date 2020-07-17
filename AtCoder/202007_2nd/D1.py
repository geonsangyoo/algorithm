import sys
DEBUG=True
# DEBUG=False
if DEBUG:
    f=open("202007_2nd/D_input.txt")
else:
    f=sys.stdin
#from 2nd count
def cnt_func(num):
    cnt=0
    while num:
        num%=bin(num).count("1")
        cnt+=1
    return cnt+1
n=int(f.readline().strip())
s=f.readline().strip()
input_val=int(s,2)
input_one_count=s.count("1")
#Base value
zero_first=input_val%(input_one_count+1)
one_first=input_val%(input_one_count-1) if input_one_count>1 else 0
ans=0
for idx,emt in enumerate(s):
    p=n-idx-1
    if emt=="0": #inverted to "1"
        ans=cnt_func((zero_first+(pow(2,p,input_one_count+1)))%(input_one_count+1))
    else: #inverted to "0"
        ans=cnt_func((one_first-(pow(2,p,input_one_count-1)))%(input_one_count-1))
    print(ans)
f.close()