import sys
sys.setrecursionlimit(1000000)
DEBUG = True
#DEBUG = False
Ascii_start = 96
if DEBUG:
    f = open("#2233/input.txt")
else:
    f = sys.stdin
N = int(f.readline().strip())
binary_input = list(f.readline().strip())
binary = [int(_) for _ in binary_input]
wormy_node_a, wormy_node_b = map(int, f.readline().split())
stack = []
element = []
depth = []
element_back = ['' for _ in range(2*N)]
depth_back = [0 for _ in range(2*N)]
answer = []
answer_node = ''
minimum_depth = 2000
element_start = Ascii_start
for _ in binary:
    if _:
        depth.append(len(stack))
        element.append(stack.pop())
        depth_back[len(element)-1] = len(stack)
        if len(stack) > 0:
            element_back[len(element)-1] = stack[len(stack)-1]
        else:
            element_back[len(element)-1] = 'a'
    else:
        element_start+=1
        element.append(chr(element_start))
        stack.append(chr(element_start))
        depth.append(len(stack))
# Put the indices of wormy nodes in the place of '0' binary
if (wormy_node_a != wormy_node_b) and (element[wormy_node_a-1] != element[wormy_node_b-1]):
    for _ in range(len(element)):
        if (element[wormy_node_a-1] == element[_]) and (binary[_] == 0):
            wormy_node_a = _+1
            break
    for _ in range(len(element)):
        if (element[wormy_node_b-1] == element[_]) and (binary[_] == 0):
            wormy_node_b = _+1
            break
else:
    for _ in range(len(element)):
        if (element[wormy_node_a-1] == element[_]) and (binary[_] == 0):
            wormy_node_a = _+1
        if (element[wormy_node_a-1] == element[_]) and (binary[_] == 1):
            wormy_node_b = _+1
            break
if wormy_node_a > wormy_node_b:
    wormy_node_a, wormy_node_b = wormy_node_b, wormy_node_a
# Two nodes are identical
if (element[wormy_node_a-1] == element[wormy_node_b-1]) or (wormy_node_a == wormy_node_b):
    print(wormy_node_a, wormy_node_b)
else:
    for _ in range (wormy_node_a-1, wormy_node_b):
        if binary[_]:
            if minimum_depth > depth_back[_]:
                answer_node = element_back[_]
                minimum_depth = depth_back[_]
        else:
            if minimum_depth > depth[_]:
                answer_node = element[_]
                minimum_depth = depth[_]
    for _ in range(len(element)):
        if element[_] == answer_node:
            answer.append(_+1)
    print(answer[0], answer[1])
f.close()