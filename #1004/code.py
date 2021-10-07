import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1004/input.txt')
else:
  f = sys.stdin

def check(x, y, r):
  return ((x - sx) ** 2 + (y - sy) ** 2 < r ** 2) ^ ((x - dx) ** 2 + (y - dy) ** 2 < r ** 2)

N = int(f.readline().strip())
for _ in range(N):
  sx, sy, dx, dy = map(int, f.readline().split())
  cnt = 0

  n = int(f.readline().strip())
  for __ in range(n):
    x, y, r = map(int, f.readline().split())
    if check(x, y, r): cnt = cnt + 1
  
  print(cnt)
