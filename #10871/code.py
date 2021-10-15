import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10871/input.txt')
else:
  f = sys.stdin

N, X = map(int, f.readline().split())
arr = list(f.readline().split())
ans = []

for _ in arr:
  if (int(_) < X): ans.append(_)

print(' '.join(ans))
