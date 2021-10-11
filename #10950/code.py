import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10950/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
for _ in range(N):
  a, b = map(int, f.readline().split())
  print(a + b)
