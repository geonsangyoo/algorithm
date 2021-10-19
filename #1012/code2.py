import sys

sys.setrecursionlimit(1000000)

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1012/input.txt')
else:
  f = sys.stdin

def visit_ew(x, y):
    global m, erws

    m[x][y] = 1
    if x - 1 >= 0 and x - 1 < h and y >= 0 and y < w and (x - 1, y) in erws and m[x - 1][y] == 0: visit_ew(x - 1, y)
    if x >= 0 and x < h and y - 1 >= 0 and y - 1 < w and (x, y - 1) in erws and m[x][y - 1] == 0: visit_ew(x, y - 1)
    if x + 1 >= 0 and x + 1 < h and y >= 0 and y < w and (x + 1, y) in erws and m[x + 1][y] == 0: visit_ew(x + 1, y)
    if x >= 0 and x < h and y + 1 >= 0 and y + 1 < w and (x, y + 1) in erws and m[x][y + 1] == 0: visit_ew(x, y + 1)

N = int(f.readline().strip())

for _ in range(N):
  cnt = 0
  erws = []
  w, h, n = map(int, f.readline().split())
  m = [[0 for x in range(w)] for y in range(h)]

  for __ in range(n):
    y, x = map(int, f.readline().split())
    erws.append((x, y))
  
  for i, v in enumerate(erws):
    if not m[v[0]][v[1]]:
      visit_ew(v[0], v[1])
      cnt += 1
  
  print(cnt)
