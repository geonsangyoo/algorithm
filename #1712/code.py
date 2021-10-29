import sys
import math

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1712/input.txt')
else:
  f = sys.stdin

A, B, C = map(float, f.readline().split())

if C > B:
  n = A / (C - B)
  if (n == math.ceil(n)):
    ans = int(n) + 1
  else:
    ans = math.ceil(n)
elif C < B:
  n = A / (C - B)
  ########################
  if (n == math.floor(n)):
    ans = int(n) - 1
  else:
    ans = math.floor(n)
  ########################  
  if ans < 1:
    ans = -1
else:
  ans = -1

print(ans)
