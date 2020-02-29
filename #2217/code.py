import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open("#2217/input.txt")
else:
    f = sys.stdin
N = int(f.readline().strip())
weight = [int(f.readline().strip()) for _ in range(N)]
max_weight = 0
weight.sort()
for _ in range(N):
    max_weight = max(max_weight, (_+1) * weight[N-(_+1)])
print(max_weight)
f.close()