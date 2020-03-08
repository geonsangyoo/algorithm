import sys
DEBUG = True
#DEBUG = False
Ascii_start = 96
if DEBUG:
    f = open("#2233/input.txt")
else:
    f = sys.stdin
T = int(f.readline().strip())
while(T>0):
    T-=1
    N = int(f.readline().strip())
    binary_input = list(f.readline().strip())
    binary = [int(_) for _ in binary_input]
    wormy_node_a, wormy_node_b = list(map(int, f.readline().split()))
    stack = list()
    element = list()
    depth = list()
    element_back = ['' for _ in range(4000)]
    depth_back = [0 for _ in range(4000)]
    answer = []
    answer_node = ''
    minimum_depth = 9999
    element_start = Ascii_start
    for _ in binary:
        if _:
            depth.append(len(stack))
            element.append(stack.pop())
            depth_back[len(element)-1] = len(stack)
            if len(stack) > 0:
                element_back[len(element)-1] = stack[len(stack)-1]
            else:
                element_back[len(element)-1] = 96
        else:
            element_start+=1
            element.append(element_start)
            stack.append(element_start)
            depth.append(len(stack))
    # Two nodes are identical
    if element[wormy_node_a-1] == element[wormy_node_b-1]:
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