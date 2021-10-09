import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2753/input.txt')
else:
  f = sys.stdin

def check_year(year):
  return 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0

N = int(f.readline().strip())
print(check_year(N))
