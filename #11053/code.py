import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#11053/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
L = list(map(int, f.readline().split()))

dp = [0] * N

for _ in range(N):
  tmp = 0
  for __ in range(_):
    if L[_] > L[__]:
      if dp[__] > tmp:
        tmp = dp[__]
  dp[_] = tmp + 1

print(max(dp))
