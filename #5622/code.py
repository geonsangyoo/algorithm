import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#5622/input.txt')
else:
  f = sys.stdin

def getElapsedTime(chr):
  cnt = 2
  if (chr in ['A', 'B', 'C']):
    cnt += 1
  elif (chr in ['D', 'E', 'F']):
    cnt += 2
  elif (chr in ['G', 'H', 'I']):
    cnt += 3
  elif (chr in ['J', 'K', 'L']):
    cnt += 4
  elif (chr in ['M', 'N', 'O']):
    cnt += 5
  elif (chr in ['P', 'Q', 'R', 'S']):
    cnt += 6
  elif (chr in ['T', 'U', 'V']):
    cnt += 7
  elif (chr in ['W', 'X', 'Y', 'Z']):
    cnt += 8
  else:
    pass
  
  return cnt

s = f.readline().strip()
ans = 0

for _ in s:
  ans += getElapsedTime(_)

print(ans)
