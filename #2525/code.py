import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open("input.txt")
else:
	f = sys.stdin

h, m = map(int, f.readline().split())
mins = int(f.readline())

h_a = (mins + m) // 60
m_a = (mins + m) % 60

print(f"{(h + h_a) % 24} {m_a}")
