import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1152/input.txt')
else:
  f = sys.stdin

s = f.readline().strip().split()
print(len(s))
