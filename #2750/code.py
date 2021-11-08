import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2750/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
num = []

for _ in range(N):
  num.append(int(f.readline().strip()))

num.sort()

for n in num:
  print(n)
