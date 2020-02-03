import sys
DEBUG = True
#DEBUG = False
if DEBUG:
    f = open("#1613/input.txt")
else:
    f = sys.stdin
def floyd_warshall():
    global relation_array, vertex_i, vertex_j
    for n in range(N):
        vertex_i = []
        vertex_j = []
        for s in range(N):
            if n != s:
                if relation_array[s][n] != 0:
                    vertex_i.append(s)
                if relation_array[n][s] != 0:
                    vertex_j.append(s)
        for i in vertex_i:
            for j in vertex_j:
                    relation_array[i][j] = 1
N, R = list(map(int,f.readline().split()))
relation_array = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    relation_array[_][_] = 0
for _ in range(R):
    i, j = list(map(int,f.readline().split()))
    relation_array[i-1][j-1] = 1
P = int(f.readline())
###Floyd and warshall algorithm###
floyd_warshall()
##################################
for _ in range(P):
    a, b = list(map(int,f.readline().split()))
    if relation_array[a-1][b-1] != 0:
        print("-1")
    elif relation_array[b-1][a-1] != 0:
        print("1")
    else:
        print("0")