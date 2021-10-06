import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1002/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, f.readline().split())

  res = 2
  dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  rest = [r1, r2, dis]

  max_val = max(r1, r2, dis)
  rest.remove(max_val)

  if x1 == x2 and y1 == y2 and r1 == r2:
    res = -1
  elif (rest[0] + rest[1]) < max_val:
    res = 0
  elif (r1 + r2) == dis or abs(r1 - r2) == dis:
    res = 1
  else:
    pass

  print(res)
