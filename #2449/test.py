import sys
dp = []
dp_ans = []
dp.append([1,2,3,2,1])
dp.append([1,3,2,1])
dp.append([1,2,1,2,1])
dp.append([1,2,3,1])
try:
    print(dp.index([1,3,2]))
except ValueError:
    print("error!")