import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10951/input.txt')
else:
  f = sys.stdin

while(True):
  l = f.readline()
  if len(l) == 0: break
  x, y = map(int, l.split())
  print(x + y)
