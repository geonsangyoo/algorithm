import sys

DEBUG = True
# DEBUG = False

# IO
if DEBUG:
  f = open("#9095/input.txt")
else:
  f = sys.stdin

# Method
def dfs(n):
  if n < 0:
    return 0
  elif n < 2:
    return 1
  else:
    if dp[n] > 0:
      return dp[n]

    dp[n] = dfs(n-1) + dfs(n-2) + dfs(n-3)
  
  return dp[n]

# Main
N = int(f.readline().strip())

for _ in range(N):
  n = int(f.readline().strip())
  dp = []
  
  for _ in range(n + 1):
    dp.append(0)

  # print the answer
  print(dfs(n))
