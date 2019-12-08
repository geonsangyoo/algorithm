import sys
sys.setrecursionlimit(1000000)
DEBUG = True
#DEBUG = False
add_range = [[0, -1], [0, 1], [1, 0], [-1, 0]]
y_range = [-1, 1]
if DEBUG == True:
    f = open("/Users/yoogeonsang/Documents/python/algorithm/#1520/input.txt", 'r')
else:
    f = sys.stdin
def chart(h, w):
    if memo[h][w] != -1:
        return memo[h][w]
    sum = 0
    for x,y in add_range:
        if h+y<0 or h+y>=height or w+x<0 or w+x>=width:
            continue
        if node_map[h][w] < node_map[h+y][w+x]:
            sum += chart(h+y, w+x)
    memo[h][w] = sum
    return sum
while True:
    # input
    line = f.readline()
    if not line:
        break
    height, width = map(int, line.split())
    node_map = [list(map(int, f.readline().split())) for _ in range(height)]
    memo = [[-1 for _ in range(width)] for _ in range(height)]
    memo[0][0] = 1
    print(chart(height-1, width-1))
f.close()