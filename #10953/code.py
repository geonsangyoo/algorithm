import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10953/input.txt')
else:
  f = sys.stdin

 
N = int(f.readline().strip())
for _ in range(N):
  A, B = map(int, f.readline().split(','))
  print(A + B)
