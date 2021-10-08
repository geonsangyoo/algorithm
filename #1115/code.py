import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1115/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())
visit = [False for _ in range(N)]
nums = list(map(int, f.readline().split()))

def travel(idx):
  if (visit[idx] == True): return
  visit[idx] = True
  travel(nums[idx])

count = 0
for i in range(N):
  if (visit[i] == False):
    travel(i)
    count = count + 1

if (count == 1):
  count = 0

print(count)
