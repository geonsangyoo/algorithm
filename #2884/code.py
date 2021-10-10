import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2884/input.txt')
else:
  f = sys.stdin

h, m = map(int, f.readline().split())

# convert
if m < 45:
  m = 60 - abs(m - 45);
  h = h - 1
else:
  m = m - 45
if h < 0: h = 23

print('{0} {1}'.format(h, m))
