import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#15552/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  x, y = map(int, f.readline().split())
  print(x + y)
