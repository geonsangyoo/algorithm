import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2439/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  for __ in range(N):
    if (__ + 1 < N - _):
      print(' ', end='')
    else:
      print('*', end='')
  print()
