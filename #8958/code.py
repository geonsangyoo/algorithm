import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#8958/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  s = f.readline()
  ans = 0
  cnt = 0
  el = [c for c in s]
  for _ in el:
    if (_ == 'O'):
      cnt += 1
      ans += cnt
    else:
      cnt = 0
  print(ans)
