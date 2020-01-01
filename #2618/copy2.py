import sys
sys.setrecursionlimit(100000)
DEBUG = True
# DEBUG = False
if DEBUG:
    f = open('input.txt','r')
else:
    f = sys.stdin
def calc_dist(from__,to__):
    if type(from__[0]) is not int:
        x1, y1 = from__[0] #1-Patrol Car initial coord.
    else:
        x1, y1 = from__
    if type(to__[0]) is not int:
        x2, y2 = to__[1] #2-Patrol Car initial coord.
    else:
        x2, y2 = to__
    return abs(x1-x2)+abs(y1-y2)
def getShortestWay(EventNum,P1_event,P2_event):
    if EventNum > E:
        return 0
    if Memo[P1_event][P2_event]!=-1:
        return Memo[P1_event][P2_event]
    Memo[P1_event][P2_event]=min(calc_dist(Events[P1_event],Events[EventNum])+getShortestWay(EventNum+1,EventNum,P2_event)\
        ,calc_dist(Events[EventNum],Events[P2_event])+getShortestWay(EventNum+1,P1_event,EventNum))
    return Memo[P1_event][P2_event]
def printShortestWay(Eventnum,P1_event,P2_event):
    if Eventnum > E:
        return 0
    if calc_dist(Events[P1_event],Events[Eventnum])+Memo[Eventnum][P2_event]\
        < calc_dist(Events[Eventnum],Events[P2_event])+Memo[P1_event][Eventnum]:
        print(1); printShortestWay(Eventnum+1,Eventnum,P2_event)
    else:
        print(2); printShortestWay(Eventnum+1,P1_event,Eventnum)
while True:
    line = f.readline()
    if not line:
        break
    N = int(line.strip())
    E = int(f.readline().strip())
    Events = [list(map(int, f.readline().split())) for _ in range(E)]
    Events.insert(0,[[1,1],[N,N]])
    Memo = [[-1 for _ in range(len(Events))] for _ in range(len(Events))]
    print(getShortestWay(1,0,0)); printShortestWay(1,0,0)
f.close()