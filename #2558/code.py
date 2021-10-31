import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2558/input.txt')
else:
  f = sys.stdin

A = int(f.readline().strip())
B = int(f.readline().strip())

print(A + B)
