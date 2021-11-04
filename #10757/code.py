import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10757/input.txt')
else:
  f = sys.stdin

A, B = map(int, f.readline().split())
print(A + B)
