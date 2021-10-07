import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1330/input.txt')
else:
  f = sys.stdin

a, b = map(int, f.readline().split())

if (a > b):
  print(">")
elif (a < b):
  print("<")
else:
  print("==")
