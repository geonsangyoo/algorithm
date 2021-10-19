import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10818/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
l = list(map(int, f.readline().split()))

print('{0} {1}'.format(min(l), max(l)))
