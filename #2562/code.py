import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#2562/input.txt')
else:
  f = sys.stdin

nums = []
for _ in range(9):
  nums.append(int(f.readline().strip()))
max_num = max(nums)

print(max_num)
print(nums.index(max_num) + 1)
