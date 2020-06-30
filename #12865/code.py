import sys
DEBUG = True
# DEBUG = False
W = 0
V = 1
if DEBUG:
    f = open("#12865/input.txt")
else:
    f = sys.stdin
def pick(idx, curr_cap, value):
    if idx == n:
        return value
    if dp[idx][curr_cap] > -1:
        return dp[idx][curr_cap]
    else:
        dp[idx][curr_cap] = pick(idx+1, curr_cap, value)
        if curr_cap >= info[idx][W]:
            dp[idx][curr_cap] = max(dp[idx][curr_cap], pick(idx+1, curr_cap-info[idx][W], value+info[idx][V]))
        return dp[idx][curr_cap]
n, cap = map(int, f.readline().split())
info = [list(map(int, f.readline().split())) for _ in range(n)]
dp = [[-1 for __ in range(cap+1)] for _ in range(n)]
print(pick(0,cap,0))
f.close()