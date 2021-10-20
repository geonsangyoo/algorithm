import sys
DEBUG = True
# DEBUG = False
if DEBUG:
  f = open('#1546/input.txt')
else:
  f = sys.stdin
N = int(f.readline().strip())
arr = list(map(int, f.readline().split()))
max_val = max(arr)
for _ in range(N):
  arr[_] = (arr[_] / float(max_val)) * 100
print(round(sum(arr) / float(N), 3))
