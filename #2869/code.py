import sys
import math

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2869/input.txt')
else:
  f = sys.stdin

A, B, V = list(map(int, f.readline().split()))
ans = (V - A) / (A - B)

if int(ans) == math.ceil(ans):
  print(int(ans) + 1)
else:
  print(math.ceil(ans) + 1)
