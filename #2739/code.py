import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2739/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(1, 10):
  print('{0} * {1} = {2}'.format(N, _, N * _))
