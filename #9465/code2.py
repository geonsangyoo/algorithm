import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("#9465/input.txt")
else:
    f=sys.stdin
def find():
    for i in range(2, column_num+1):
        b[2]=max(c[1]+num[0][i-1] , b[0]+num[0][i-1]+num[1][i-2] , c[0]+num[0][i-1])
        c[2]=max(b[1]+num[1][i-1] , c[0]+num[1][i-1]+num[0][i-2] , b[0]+num[1][i-1])
        b[0]=b[1];b[1]=b[2]
        c[0]=c[1];c[1]=c[2]
N=int(f.readline().strip())
while(N>0):
    N-=1
    column_num=int(f.readline().strip())
    b=[0,0,0]
    c=[0,0,0]
    num=[list(map(int, f.readline().split())) for _ in range(2)]
    #base value (initialization)
    b[0],b[1]=0,num[0][0]
    c[0],c[1]=0,num[1][0]
    find()
    print(max(b[2],c[2]))