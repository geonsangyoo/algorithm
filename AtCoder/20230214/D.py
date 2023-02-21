import sys

DEBUG = True

if DEBUG:
    f = open("input_D.txt")
else:
    f = sys.stdin

# input
N = int(f.readline().strip())
A = list(map(int, f.readline().strip().split()))
M = int(f.readline().strip())
B = list(map(int, f.readline().strip().split()))
B_SET = set(B)
X = int(f.readline().strip())

# dp
ok = [0] * (X + 1)
ok[0] = 1


# check func
def cal(x):
    if x in B_SET:
        return
    for n in A:
        nn = x - n
        if nn < 0:
            break
        if ok[nn]:
            ok[x] = 1


# main
for r in range(1, X + 1):
    cal(r)

if ok[X]:
    print("Yes")
else:
    print("No")
