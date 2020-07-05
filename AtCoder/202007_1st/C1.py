import sys
from itertools import combinations
DEBUG = True
# DEBUG = False
if DEBUG:
    f=open("202007_1st/C_input.txt")
else:
    f=sys.stdin
WHITE='.'
BLACK='#'
def count_black(H_index,W_index):
    count_tmp=0
    for _ in range(H):
        if _ in H_index:
            continue
        for __ in range(W):
            if __ in W_index:
                continue
            if S[_][__]==BLACK:
                count_tmp+=1
    return count_tmp
ans=0
H,W,K=map(int,f.readline().split())
S=[f.readline().strip() for _ in range(H)]
H_indices=[_ for _ in range(0,H)]
W_indices=[_ for _ in range(0,W)]
combi_list_H=[[-1]]
combi_list_W=[[-1]]
for _ in range(1,H):
    combi_list_H.extend(list(combinations(H_indices,_)))
for _ in range(1,W):
    combi_list_W.extend(list(combinations(W_indices,_)))
for _ in combi_list_H:
    for __ in combi_list_W:
        if count_black(_,__)==K:
            ans+=1
print(ans)
f.close()