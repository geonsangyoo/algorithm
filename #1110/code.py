import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1110/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
base = N
base_str = str(base).zfill(2)
cnt = 0

while(True):
  cnt += 1

  num_str = str(N).zfill(2)
  left = int(num_str[0])
  right = int(num_str[1])
  ans_str = str(left + right).zfill(2)

  if (num_str[1] == base_str[0]) and (ans_str[1] == base_str[1]):
    break

  N = int(num_str[1] + ans_str[1])

print(cnt)
