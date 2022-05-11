import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('input.txt')
else:
  f = sys.stdin

N = int(f.readline())
nums = list(map(int, f.readline().split()))

count = 0
for i in nums:
  if i == 1:
    continue
  if i == 2:
    count +=1
    continue

  x = False
  for j in range(2, i):
    if (i % j) == 0:
      x = True
      break
  if not x:
    count += 1

print(count)
