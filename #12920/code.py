import sys
sys.setrecursionlimit(999999)
DEBUG = True
# DEBUG = False
W = 0
V = 1
N = 2
UNPICKABLE = 0
PICKABLE = 1
if DEBUG:
    f = open("#12920/input.txt")
else:
    f = sys.stdin
def pick(idx, curr_cap):
    if idx >= num:
        return 0
    if dp[idx][curr_cap] != -1:
        return dp[idx][curr_cap]
    else:
        dp[idx][curr_cap] = pick(idx+1, curr_cap)
        if curr_cap >= entry[idx][W] and pick_flag[idx] == PICKABLE:
            dp[idx][curr_cap] = max(dp[idx][curr_cap], pick(idx+1, curr_cap-entry[idx][W])+entry[idx][V])
        return dp[idx][curr_cap]
n, cap = map(int, f.readline().split())
info = [list(map(int, f.readline().split())) for _ in range(n)]
for _ in range(n):
    if info[_][W]*info[_][N] > cap:
        info[_][N] = int(cap/info[_][W])
exception_numbers = [1<<_ for _ in range(1,14)]
entry = list()
pick_flag = list()
start = 1
for _ in range(n):
    binary = bin(info[_][N])[2:]
    if info[_][N] in exception_numbers:
        except_flg = True
        for_len = len(binary)-1
    else:
        except_flg = False
        for_len = len(binary)
    for __ in range(for_len):
        inner_idx = int(binary[len(binary)-1-__])
        weight_val = start<<__
        entry.append([info[_][W]*weight_val, info[_][V]*weight_val])
        pick_flag.append(inner_idx)
        if except_flg and __==0:
            entry.append(entry[len(entry)-1])
            pick_flag.append(PICKABLE)
num = len(entry)
dp = [[-1 for __ in range(cap+1)] for _ in range(num)]
print(pick(0,cap))
f.close()