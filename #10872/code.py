import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10872/input.txt')
else:
  f = sys.stdin

def factorial(n):
  if n < 1:
    return 1
  return n * factorial(n - 1)

N = int(f.readline().strip())
print(factorial(N))
