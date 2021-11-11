import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2580/input.txt')
else:
  f = sys.stdin

# SUDOKU_MAP insertion
SUDOKU_MAP = [list(map(int, f.readline().split())) for _ in range(9)]

candidates = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

ROWMAP = [[False for __ in range(9)] for _ in range(9)]
COLMAP = [[False for __ in range(9)] for _ in range(9)]
RECMAP = [[False for __ in range(9)] for _ in range(9)]

Q = []

for _ in range(9):
  for __ in range(9):
    if SUDOKU_MAP[_][__] != 0:
      ROWMAP[_][SUDOKU_MAP[_][__] - 1] = True
      COLMAP[__][SUDOKU_MAP[_][__] - 1] = True
      RECMAP[candidates.index((_ // 3 * 3, __ // 3 * 3))][SUDOKU_MAP[_][__] - 1] = True
    else:
      # Q insertion
      Q.append((_, __))

# Put a new number
def put_number(idx):
  if len(Q) <= idx:
    for a in SUDOKU_MAP:
      print(*a)
    exit()

  x, y = Q[idx]
  
  xs = x // 3 * 3
  ys = y // 3 * 3
  i = candidates.index((xs, ys))

  for v in range(1, 10):
    if not ROWMAP[x][v - 1] and not COLMAP[y][v - 1] and not RECMAP[i][v - 1]:
      SUDOKU_MAP[x][y] = v
      ROWMAP[x][v - 1] = True
      COLMAP[y][v - 1] = True
      RECMAP[i][v - 1] = True
      put_number(idx + 1)
      SUDOKU_MAP[x][y] = 0
      ROWMAP[x][v - 1] = False
      COLMAP[y][v - 1] = False
      RECMAP[i][v - 1] = False

put_number(0)
