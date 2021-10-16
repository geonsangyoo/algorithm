import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10952/input.txt')
else:
  f = sys.stdin

while(True):
  x, y = map(int, f.readline().split())
  if x == 0 and y == 0: break
  print(x + y)
