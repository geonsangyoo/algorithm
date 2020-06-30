import sys
DEBUG = True
#DEBUG = False
W = 0
V = 1
N = 2
if DEBUG:
    f = open("#12920/input.txt")
else:
    f = sys.stdin
n, cap = map(int, f.readline().split())
info = []
for _ in range(n):
    input_w,input_v,input_n = map(int, f.readline().split())
    if input_w > cap:
        continue
    for __ in range(len(info)):
        if info[__][W] == input_w and info[__][V] == input_v:
            info[__][N] += input_n
            if input_w * info[__][N] > cap:
                info[__][N] = int(cap/input_w)
            input_n = 0
            break
    if input_n:
        info.append([input_w,input_v,input_n])
n = len(info)
for _ in range(n):
    if info[_][W] * info[_][N] > cap:
        info[_][N] = int(cap/info[_][W])
entry = list()
start = 1
for _ in range(n):
    num = info[_][N]
    while num > 0:
        temp = num >> 1
        weight_val = num-temp
        entry.append([info[_][W]*weight_val, info[_][V]*weight_val])
        num = temp
num = len(entry)
dp = [0 for __ in range(cap+1)]
# change overall logic from recursive to for-loop
for _ in range(num):
    for __ in range(cap,entry[_][W]-1,-1):
        dp[__] = max(dp[__], dp[__-entry[_][W]]+entry[_][V])
print(dp[cap])
f.close()