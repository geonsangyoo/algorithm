import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2438/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  for __ in range(_ + 1):
    print('*', end='')
  print()
