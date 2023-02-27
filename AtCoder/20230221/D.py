import sys

DEBUG = True

if DEBUG:
    f = open("input_D.txt")
else:
    f = sys.stdin

# input
N = int(f.readline().strip())
D = {}
S = set()
visited = set()

for _ in range(N):
    s, t = f.readline().strip().split()
    D[s] = t
    S.add(s)

for handle in S:
    next_handle = D[handle]
    while next_handle not in visited:
        visited.add(next_handle)
        if next_handle not in D.keys():
            break
        next_handle = D[next_handle]
        if next_handle == handle:
            print("No")
            exit()

print("Yes")
