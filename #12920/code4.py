import sys
DEBUG = True
if DEBUG:
    f = open("#12920/input.txt")
else:
    f = sys.stdin
n, cap = map(int, f.readline().split())
info_W = []
info_V = []
info_N = []
entry_W = []
entry_V = []
for _ in range(n):
    input_w,input_v,input_n = map(int, f.readline().split())
    for __ in range(len(info_W)):
        if info_W[__] == input_w and info_V[__] == input_v:
            info_N[__] = info_N[__] + input_n
            input_n = 0
            break
    if input_n:
        info_W.append(input_w)
        info_V.append(input_v)
        info_N.append(input_n)
n = len(info_W)
for _ in range(n):
    num = info_N[_]
    weight_temp = info_W[_]
    value_temp = info_V[_]
    while num > 0:
        weight_val = num-(num>>1)
        entry_W.append(weight_temp*weight_val)
        entry_V.append(value_temp*weight_val)
        num = num >> 1
num = len(entry_W)
dp = [0 for __ in range(cap+1)]
for _ in range(num):
    num_entry = entry_W[_]-1
    weight_entry = entry_W[_]
    value_entry = entry_V[_]
    for __ in range(cap,num_entry,-1):
        dp[__] = max(dp[__], dp[__-weight_entry]+value_entry)
print(dp[cap])