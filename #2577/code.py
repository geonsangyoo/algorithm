import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2577/input.txt')
else:
  f = sys.stdin

n = 1
ans = [0 for _ in range(10)]
for _ in range(3):
  n *= int(f.readline().strip())

for _ in str(n):
  ans[int(_)] += 1

for _ in ans:
  print(_)
