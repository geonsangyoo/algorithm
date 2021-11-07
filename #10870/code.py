import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#10872/input.txt')
else:
  f = sys.stdin

def fibonacci(n):
  if n == 0:
    return 0
  if n < 3:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)

N = int(f.readline().strip())
print(fibonacci(N))
