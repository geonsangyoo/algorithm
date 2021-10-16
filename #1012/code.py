import sys

sys.setrecursionlimit(1000000)

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1012/input.txt')
else:
  f = sys.stdin

def visit_ew(x, y):
  if x < 0 or y < 0:
    return
  if (x, y) in erws and isVisit[erws.index((x, y))] == 0:
    isVisit[erws.index((x, y))] = 1
    visit_ew(x - 1, y)
    visit_ew(x, y - 1)
    visit_ew(x + 1, y)
    visit_ew(x, y + 1)

N = int(f.readline().strip())

for _ in range(N):
  cnt = 0
  erws = []
  w, h, n = map(int, f.readline().split())
  m = [[0 for x in range(w)] for y in range(h)]
  isVisit = [0 for __ in range(n)]

  for __ in range(n):
    y, x = map(int, f.readline().split())
    erws.append((x, y))
    m[x][y] = 1
  
  for i, v in enumerate(erws):
    if not isVisit[i]:
      visit_ew(v[0], v[1])
      cnt += 1
  
  print(cnt)
