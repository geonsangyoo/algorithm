import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1003/input.txt')
else:
  f = sys.stdin

def sum_lists(*args):
  return list(map(sum, zip(*args)))

def fibonacci(n):
  if n < 0:
    return [0, 0]

  if (len(a_0) > n and len(a_1) > n):
    return [a_0[n], a_1[n]]

  a_new = sum_lists(fibonacci(n - 1), fibonacci(n - 2))
  
  a_0.append(a_new[0])
  a_1.append(a_new[1])
  
  return a_new

N = int(f.readline().strip())

for _ in range(N):
  n = int(f.readline().strip())

  a_0 = [1, 0, 1]
  a_1 = [0, 1, 1]

  fibonacci(n)

  print('{0} {1}'.format(a_0[n], a_1[n]))
