import sys
DEBUG = True
# DEBUG = False
if DEBUG:
  f = open('#11720/input.txt')
else:
  f = sys.stdin
n = int(f.readline().strip())
ans = 0
for _ in range(n):
  ans += int(f.read(1))
print(ans)