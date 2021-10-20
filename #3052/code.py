import sys
DEBUG = True
# DEBUG = False
if DEBUG:
  f = open('#3052/input.txt')
else:
  f = sys.stdin
i = []
for _ in range(10):
  i.append(int(f.readline().strip()) % 42)
print(len(list(dict.fromkeys(i))))
