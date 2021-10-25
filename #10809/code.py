import sys
import re

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10809/input.txt')
else:
  f = sys.stdin

s = f.readline().strip()

for _ in range(ord('a'), ord('z') + 1):
  c = chr(_)
  ans = re.search(c, s)
  if ans is None:
    print(-1, end='')
  else:
    print(ans.start(), end='')
  if (_ < ord('z')):
    print(' ', end='')
  else:
    print()
