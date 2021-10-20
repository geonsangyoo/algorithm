import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#4344/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

for _ in range(N):
  inputs = list(map(int, f.readline().split()))
  n = inputs[0]
  upper_n = 0
  avg = (sum(inputs) - n) / float(n)
  for _ in range(n):
    if (inputs[_ + 1] > avg):
      upper_n += 1
  if upper_n < 1:
    print('0.000%')
  else:
    print('{0:.3f}%'.format(round(upper_n / float(n) * 100, 3)))
