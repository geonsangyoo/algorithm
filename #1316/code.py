import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1316/input.txt')
else:
  f = sys.stdin

T = int(f.readline().strip())
cnt = 0

for _ in range(T):
  isGroup = True
  r = []
  
  for c in f.readline().strip():
    if c in r:
      if not (r[-1] == c):
        isGroup = False
        break
    else:
      r.append(c)

  if (isGroup): cnt += 1

print(cnt)
