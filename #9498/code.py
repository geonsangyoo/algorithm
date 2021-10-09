import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#9498/input.txt')
else:
  f = sys.stdin

N = int(f.readline().strip())

if N >= 90:
  print("A")
elif N >= 80:
  print("B")
elif N >= 70:
  print("C")
elif N >= 60:
  print("D")
else:
  print("F")
