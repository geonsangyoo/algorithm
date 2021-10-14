import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2742/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N, 0, -1):
  print(_)
