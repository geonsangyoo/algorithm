import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2738/input.txt')
else:
  f = sys.stdin

def mat_add(A, B):
  for _ in range(N):
    row_str = ''
    for __ in range(M):
      row_str = row_str + ' ' + str(A[_][__] + B[_][__])
    print(row_str.strip())

N, M = map(int, f.readline().split())
A = [list(map(int, f.readline().split())) for _ in range(N)]
B = [list(map(int, f.readline().split())) for _ in range(N)]

mat_add(A, B)
