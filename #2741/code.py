import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2741/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  print(_+1)
