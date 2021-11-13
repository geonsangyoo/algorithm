import sys, math

sys.setrecursionlimit(99999)

DEBUG = True
# DEBUG = False

A = 5
B = 3

if DEBUG:
  f = open('#2839/input.txt')
else:
  f = sys.stdin

def get_bag_number(n):
  if n < 0:
    return math.inf
  if n == 0:
    return 0
  if dp[n] > 0:
    return dp[n]
  
  dp[n] = min(get_bag_number(n - A) + 1, get_bag_number(n - B) + 1)
  return dp[n]

N = int(f.readline().strip())
dp = [0] * (N + 1)

get_bag_number(N)

print(dp[N]) if dp[N] != math.inf else print(-1)
