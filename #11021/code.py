import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#11021/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  x, y = map(int, f.readline().split())
  print("Case #{0}: {1}".format(_ + 1, x + y))
