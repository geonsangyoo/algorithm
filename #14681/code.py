import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#14681/input.txt')
else:
  f = sys.stdin

def getQuadrantNum(x, y):
  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  elif x > 0 and y < 0:
    return 4
  else:
    pass

x = int(f.readline().strip())
y = int(f.readline().strip())

print(getQuadrantNum(x, y))
