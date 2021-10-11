import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#8393/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

sum = 0
for _ in range(1, N + 1):
  sum = sum + _

print(sum)
