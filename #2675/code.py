import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2675/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
for _ in range(N):
  n, s = f.readline().split()
  n = int(n)
  for c in s:
    for __ in range(n):
      print(c, end='')
  print()
