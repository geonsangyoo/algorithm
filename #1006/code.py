import sys, os
sys.setrecursionlimit(1000000)
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open('#1006/input.txt', 'r')
else:
    f = sys.stdin
def isExist(list, element):
    for e in list:
        if e == element:
            return True
    return False
def adjacent_index(index):
    adj_ind = list()
    adj_ind.append((index+N)%(2*N))
    if index==0 or index==N:
        adj_ind.append(index+N-1)
        adj_ind.append(index+1)
    elif index==N-1 or index==(2*N)-1:
        adj_ind.append(index-N+1)
        adj_ind.append(index-1)
    else:
        adj_ind.append(index+1)
        adj_ind.append(index-1)
    return adj_ind
def organize(index, left, unpick):
    if memo[index][left] != -1:
        return memo[index][left]
    adj_list = adjacent_index(index)
    unpick.remove(index)
    unpick_tmp = unpick.copy()
    #adj X
    for next_ind in unpick:
        memo[index][left] = min(1 + organize(next_ind, left-1, unpick), organize(next_ind, left, unpick))
    #adj O
    for adj_ind in adj_list:
        if isExist(unpick, adj_ind) == True:
            unpick = unpick_tmp.copy()
            unpick.remove(adj_ind)
            for next_ind in unpick:
                memo[index][left] = min(memo[index][left], 1 + organize(next_ind, left-2, unpick))
    return memo[index][left]
T = int(f.readline().strip())
while(T>0):
    T-=1
    N, W = map(int,f.readline().split())
    EnemyMap = list(map(int, f.readline().split()))
    buffer = list(map(int, f.readline().split()))
    EnemyMap.extend(buffer)
    NUMBER = 0
    memo = [[-1 for _ in range((2*N)+1)] for _ in range(2*N)]
    for i in range(2*N):
        memo[i][0] = 1
    unpick = [i for i in range(2*N)]
    print(organize(0,N*2,unpick))
f.close()