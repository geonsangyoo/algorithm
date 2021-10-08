import sys

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#1014/input.txt')
else:
  f = sys.stdin

def split(word): 
  return [char for char in word]  

N = int(f.readline().strip())

for _ in range(N):
  h, w = map(int, f.readline().split())
  c_map = [split(str(f.readline().strip())) for _ in range(h)]

  cnt = 0

  # 1 -> general case
  for __ in range(0, w):
    cnt_app = 0
    for ___ in range(__, w, 2):
      for ____ in range(0, h):
        if c_map[____][___] != 'x': cnt_app = cnt_app + 1
    cnt = max(cnt, cnt_app)

    # 2 -> exception case
    if (w > 2 and w % 2 == 0):
      cnt_app = 0
      for ___ in range(__, w, 2):
        for ____ in range(0, h):
          if c_map[____][___] != 'x': cnt_app = cnt_app + 1
        if (___ + 3 == w - 1):
          for ____ in range(0, h):
            if c_map[____][w - 1] != 'x': cnt_app = cnt_app + 1
          break
      cnt = max(cnt, cnt_app)
  
  print(cnt)
