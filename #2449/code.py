import sys, math
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open("#2449/input.txt")
else:
    f = sys.stdin
# input
bulb_number, color = map(int,f.readline().split())
input_data = list(map(int,f.readline().split()))
dp = [[0 for __ in range(bulb_number)] for _ in range(bulb_number)]
# main
for n in range(bulb_number-1):
    if input_data[n] != input_data[n+1]:
        dp[n][n+1] = 1
for leng in range(2, bulb_number):
    for start in range(bulb_number):
        if (start+leng) >= bulb_number:
            break
        dp[start][start+leng] = math.inf
        for grp in range(leng):
            tmp = dp[start][start+grp] + dp[start+grp+1][start+leng]
            if input_data[start] != input_data[start+grp+1]:
                tmp += 1
            dp[start][start+leng] = min(dp[start][start+leng], tmp)
print(dp[0][bulb_number-1])
f.close()