import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("202007_1st/B_input.txt")
else:
    f=sys.stdin
N=int(f.readline())
V=[f.readline().strip() for _ in range(N)]
R=[0,0,0,0]
for _ in range(N):
    if V[_]=='AC':
        R[0]+=1
    elif V[_]=='WA':
        R[1]+=1
    elif V[_]=='TLE':
        R[2]+=1
    elif V[_]=='RE':
        R[3]+=1
    else:
        pass
print("AC x {0}".format(R[0]))
print("WA x {0}".format(R[1]))
print("TLE x {0}".format(R[2]))
print("RE x {0}".format(R[3]))
f.close()