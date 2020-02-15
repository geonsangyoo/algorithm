import sys
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open("#5052/input.txt")
else:
    f = sys.stdin
class phone_number:
    def __init__(self, number):
        self.number = number
        self.nextNumbers = {}
        self.end = False
    def get_number(self):
        return self.number
    def get_nextNumbers(self):
        return self.nextNumbers
    def get_end(self):
        return self.end
    def set_end(self, boolean):
        self.end = boolean
N = int(f.readline())
while(N>0):
    N-=1
    fg = True
    trial = int(f.readline())
    problem = [f.readline().strip() for _ in range(trial)]
    root = {}
    for string in problem:
        idx = 0
        leng = len(string)
        for ch in string:
            idx+=1
            if idx == 1:
                group = root
            else:
                group = prev.get_nextNumbers()
            if ch not in group.keys():
                group[ch] = phone_number(ch)
                if idx == leng:
                    group[ch].set_end(True)
            else:
                if (group[ch].get_end() == True) or (idx == leng):
                    print("NO")
                    fg = False
                    break
            prev = group[ch]
        if fg == False:
            break
    if fg == True:
        print("YES")