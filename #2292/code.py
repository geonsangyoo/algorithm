import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2292/input.txt')
else:
  f = sys.stdin

ans = int(f.readline().strip())
idx = 0

while(True):
  if ((3 * idx**2) + (3 * idx) + 1) >= ans:
    break
  idx += 1

print(idx + 1)
