import sys

f = sys.stdin
n = 10000
cons = [0] * n

def d(num):
  if num > n: return
  if cons[num - 1]: return
  else:
    cons[num - 1] = 1
    d(num + sum(list(map(int, str(num)))))

for _ in range(n):
  if not (cons[_]):
    print(_ + 1)
    d(_ + 1)
