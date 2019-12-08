import sys
sys.setrecursionlimit(100000)
DEBUG = True
#DEBUG = False
if DEBUG == True:
    f = open("/Users/yoogeonsang/Documents/python/algorithm/#1890/input.txt", 'r')
else:
    f = sys.stdin
def chart(h,w):
    if memo[h][w]!=-1:
        return memo[h][w]
    sum = 0
    for h_r in range(0, h):
        jump_num = node_map[h_r][w]
        if h_r+jump_num == h:
            sum+=chart(h_r,w)
    for w_r in range(0, w):
        jump_num = node_map[h][w_r]
        if w_r+jump_num == w:
            sum+=chart(h,w_r)
    memo[h][w] = sum
    return sum
while True:
    line = f.readline()
    if not line:
        break
    N = int(line.strip())
    node_map = [list(map(int,f.readline().split())) for _ in range(N)]
    memo = [[-1 for _ in range(N)] for _ in range(N)]
    memo[0][0] = 1
    print(chart(N-1,N-1))
f.close()