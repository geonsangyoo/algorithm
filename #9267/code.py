import sys, math

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#9267/input.txt')
else:
  f = sys.stdin

def euc(a, b):
  if b == 0:
    return a, 1, 0
  g, x, y = euc(b, a % b)
  return g, y, x - ((a // b) * y)

a, b, s = map(int, f.readline().split())

if a == 0 and b == 0:
  if s == 0:
    print('YES')
    exit()
  else:
    print('NO')
    exit()
if a == 0:
  if s % b == 0:
    print('YES')
    exit()
  else:
    print('NO')
    exit()
if b == 0:
  if s % a == 0:
    print('YES')
    exit()
  else:
    print('NO')
    exit()

g, x, y = euc(a, b)

if s % g != 0:
  print('NO')
  exit()

x *= (s // g)
y *= (s // g)

for _ in range(-g * x // b + 1, g * y // a + 1):
  if euc(x + (b * _ // g), y - (a * _ // g))[0] == 1:
    print('YES')
    exit()

print('NO')
