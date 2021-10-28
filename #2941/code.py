import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2941/input.txt')
else:
  f = sys.stdin

s = f.readline().strip()
n = len(str(s))
cnt = 0
_ = 0

def isTypeA(c):
  rtv = True if (c == 'dz=') else False
  return rtv

def isTypeB(c):
  rtv = True if (c in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']) else False
  return rtv

while(_ < n):
  if (_ + 2 < n):
    if isTypeA(s[_:_ + 3]):
      cnt += 1
      _ += 3
      continue
  if (_ + 1 < n):
    if isTypeB(s[_: _ + 2]):
      cnt += 1
      _ += 2
      continue
  # Neither of both conditions above
  cnt += 1
  _ += 1

print(cnt)
