#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findTotalPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#

def getPowerOfContiguousGroupOfServers(power, l, r):
    global result_sum_map

    arr = power[l:r+1]

    if (l == r):
        result_sum_map[l][r] = arr[0]
    else:
        result_sum_map[l][r] = result_sum_map[l][r-1] + arr[-1]

    return min(arr) * result_sum_map[l][r]

def findTotalPower(power):
    # Write your code here
    global result_sum_map
    # Modular operand
    mod = (10**9) + 7
    # init
    result = 0
    power_len = len(power)
    for _ in range(power_len):
        for __ in range(_, power_len):
            result += getPowerOfContiguousGroupOfServers(power, _, __)

    print(f"test {result_sum_map}")
    return result % mod
    
if __name__ == '__main__':
    f = open('input.txt')
    power_count = int(f.readline().strip())
    power = []
    # init
    result_sum_map = [[0 for _ in range(power_count)] for _ in range(power_count)] # partial sum

    for _ in range(power_count):
        power_item = int(f.readline().strip())
        power.append(power_item)

    result = findTotalPower(power)
    print(result)

    f.close()
