import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("202007_1st/A_input.txt")
else:
    f=sys.stdin
N=int(f.readline().strip())
R=N%1000
if R==0:
    print(R)
else:
    print(1000-(N%1000))
f.close()