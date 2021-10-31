import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#9316/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
for _ in range(N):
  print('Hello World, Judge {0}!'.format(_ + 1))
