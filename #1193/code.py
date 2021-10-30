import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1193/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
n = 1

while(((n**2 + n) / 2) < N):
  n += 1

fn = (n**2 + n) / 2

# even
if (n % 2 == 0):
  up = n - (fn - N)
  down = (fn - N) + 1
# odd
else:
  up = (fn - N) + 1
  down = n - (fn - N)

print('{0}/{1}'.format(int(up), int(down)))
