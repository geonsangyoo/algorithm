import sys, math

DEBUG = True
# DEBUG = False

if (DEBUG):
  f = open('#10250/input.txt')
else:
  f = sys.stdin

T = int(f.readline().strip())
for _ in range(T):
  H, W, N = map(int, f.readline().split())
  floor = H if (N % H == 0) else N % H
  room = str(math.ceil(N / H)).rjust(2, '0')
  
  print('{0}{1}'.format(floor, room))
