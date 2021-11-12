import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2751/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
nums = []
for _ in range(N):
  nums.append(int(f.readline().strip()))

nums.sort()
for _ in range(N):
  print(nums[_])
