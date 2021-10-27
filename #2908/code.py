import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2908/input.txt')
else:
  f = sys.stdin

i, j = f.readline().split()
s1, s2 = int(i[::-1],), int(j[::-1])
print(s1) if (s1 > s2) else print(s2)
