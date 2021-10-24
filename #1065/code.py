import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1065/input.txt')
else:
  f = sys.stdin

n = int(f.readline().strip())
nstr = str(n)
num = len(nstr)

if (num < 3):
  print(n)
else:
  ans = 99
  end = n
  if num > 3:
    end = 999
  for _ in range(100, end + 1):
    nnstr = str(_)
    if (int(nnstr[1]) * 2 == int(nnstr[0]) + int(nnstr[2])):
      ans += 1
  print(ans)
