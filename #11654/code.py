import sys
DEBUG = True
# DEBUG = False
if DEBUG:
  f = open('#11654/input.txt')
else:
  f = sys.stdin
print(ord(f.read(1)))