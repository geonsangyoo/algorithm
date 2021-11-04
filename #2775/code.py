import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2775/input.txt')
else:
  f = sys.stdin

T = int(f.readline().strip())

for _ in range(T):
  k = int(f.readline().strip())
  n = int(f.readline().strip())
  apt = [[0 for ___ in range(n)] for __ in range(k + 1)]

  for __ in range(n):
    apt[0][__] = __ + 1
  
  for __ in range(1, k + 1):
    for ___ in range(n):
      for ____ in range(___ + 1):
        apt[__][___] += apt[__ - 1][____]
  
  print(apt[k][n - 1])
