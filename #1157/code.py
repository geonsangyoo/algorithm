import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1157/input.txt')
else:
  f = sys.stdin

s = f.readline().strip().upper()
dp = [0] * ((ord('Z') + 1) - ord('A'))
base = ord('A')

for _ in s:
  dp[ord(_) - base] += 1

a = max(dp)
indexes = list(filter(lambda i: dp[i] == a, range(len(dp))))
print(chr(base + indexes[0])) if len(indexes) < 2 else print('?')
