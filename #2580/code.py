import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2580/input.txt')
else:
  f = sys.stdin

# N = 9

# SUDOKU_MAP insertion
SUDOKU_MAP = [list(map(int, f.readline().split())) for _ in range(9)]

# Q insertion
Q = [(_, __) for __ in range(9) for _ in range(9) if SUDOKU_MAP[_][__] == 0]
# Q = []
# for _ in range(9):
#   for __ in range(9):
#     if SUDOKU_MAP[_][__] == 0:
#       Q.append((_, __))

# Check if the number inserted meets the rules of SUDOKU
# def check(x, y, v):
#   for _ in range(N):
#     if SUDOKU_MAP[_][y] == v and _ != x:
#       return False

#   for _ in range(N):
#     if SUDOKU_MAP[x][_] == v and _ != y:
#       return False

#   for _ in range(x // 3 * 3, x // 3 * 3 + 3):
#     for __ in range(y // 3 * 3, y // 3 * 3 + 3):
#       if SUDOKU_MAP[_][__] == v and _ != x and __ != y:
#         return False

#   return True

def get_candidates(x, y):
  numbers = [i + 1 for i in range(9)]
  xs = x // 3 * 3
  xe = xs + 3
  ys = y // 3 * 3
  ye = ys + 3

  for _ in range(9):
    if SUDOKU_MAP[x][_] in numbers:
      numbers.remove(SUDOKU_MAP[x][_])
    if SUDOKU_MAP[_][y] in numbers:
      numbers.remove(SUDOKU_MAP[_][y])

  for _ in range(xs, xe):
    for __ in range(ys, ye):
      if SUDOKU_MAP[_][__] in numbers:
        numbers.remove(SUDOKU_MAP[_][__])
    
  return numbers

# Put a new number
def put_number(idx):
  if len(Q) <= idx:
    for a in SUDOKU_MAP:
      print(*a)
    exit()

  x, y = Q[idx]
  candidates = get_candidates(x, y)

  for v in candidates:
    SUDOKU_MAP[x][y] = v
    put_number(idx + 1)
    SUDOKU_MAP[x][y] = 0

  # for v in range(1, N + 1):
  #   SUDOKU_MAP[x][y] = v
  #   if check(x, y, v) == True:
  #     put_number(idx + 1)
  #     SUDOKU_MAP[x][y] = 0

put_number(0)
