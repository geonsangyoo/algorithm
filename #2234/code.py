import sys
DEBUG = True
#DEBUG = False
if DEBUG:
    f = open("#2234/input.txt")
else:
    f = sys.stdin
# Global variable
direction = [[-1,0],[1,0],[0,-1],[0,1]]
south, east, north, west = 0,1,2,3
area_group = list()
area_group_size = list()
max_area = 0
max_area_withoutwall = 0
# Class
class room_info(object):
    room_count = 0
    def __init__(self, __wall):
        self.__wall = __wall
        self.__room_number = 0
        self.__visit = False
        self.__maximum_numberOfRoom_withNoOneWall = 0
    @staticmethod
    # -prob1.
    def get_room_count():
        return room_info.room_count
    @property
    def wall(self):
        return self.__wall
    @property
    def room_number(self):
        return self.__room_number
    @property
    def visit(self):
        return self.__visit
    @property
    def maximum_numberOfRoom_withNoOneWall(self):
        return self.__maximum_numberOfRoom_withNoOneWall
    @wall.setter
    def wall(self, wall):
        if not isinstance(wall, list):
            raise TypeError("Must be a list!")
        self.__wall = wall
    @room_number.setter
    def room_number(self, room_number):
        if not isinstance(room_number, int):
            raise TypeError("Must be an int!")
        self.__room_number = room_number
    @visit.setter
    def visit(self, visit):
        if not isinstance(visit, bool):
            raise TypeError("Must be a bool!")
        self.__visit = visit
    @maximum_numberOfRoom_withNoOneWall.setter
    def maximum_numberOfRoom_withNoOneWall(self, maximum_numberOfRoom_withNoOneWall):
        if not isinstance(maximum_numberOfRoom_withNoOneWall, int):
            raise TypeError("Must be an int!")
        self.__maximum_numberOfRoom_withNoOneWall = maximum_numberOfRoom_withNoOneWall
# Function
def check_boundary(x, y, row, col):
    if (x+row) < 0 or (x+row) >= m or (y+col) < 0 or (y+col) >= n:
        return False
    else:
        return True
def is_exist(queue,cord):
    if cord in queue:
        return True
    else:
        return False
def get_wall_direction(wall_num):
    wall = list(map(int, list(format(wall_num, 'b').zfill(4))))
    return wall
def traverse(x, y):
    room_info.room_count += 1
    area = list()
    queue = [[x,y]]
    x_cord, y_cord = 0, 0
    while len(queue) > 0:
        x_cord, y_cord = queue[0]
        area.append(queue[0])
        queue.remove(queue[0])
        castle_rooms[x_cord][y_cord].visit = True
        castle_rooms[x_cord][y_cord].room_number = room_info.get_room_count()
        for row, col in direction:
            if not check_boundary(x_cord,y_cord,row,col):
                continue
            if castle_rooms[x_cord+row][y_cord+col].visit:
                continue
            if ((row == -1) and (col == 0) and (castle_rooms[x_cord][y_cord].wall[north] == False)) or ((row == 1) and (col == 0) and (castle_rooms[x_cord][y_cord].wall[south] == False)) or ((row == 0) and (col == -1) and (castle_rooms[x_cord][y_cord].wall[west] == False)) or ((row == 0) and (col == 1) and (castle_rooms[x_cord][y_cord].wall[east] == False)):
                if not is_exist(queue,[x_cord+row, y_cord+col]):
                    queue.append([x_cord+row, y_cord+col])
    return area
# Input
n, m = list(map(int, f.readline().split()))
castle_wall = [list(map(int, f.readline().split())) for _ in range(m)]
castle_rooms = [[room_info(get_wall_direction(castle_wall[_][__])) for __ in range (n)] for _ in range(m)]
# Traverse
for x in range(m):
    for y in range(n):
        if not castle_rooms[x][y].visit:
            area_group.append(traverse(x,y))
            area_group_size.append(len(area_group[room_info.get_room_count()-1]))
            # -prob2.
            max_area = max(max_area, area_group_size[room_info.get_room_count()-1])
# -prob3.
for x in range(m):
    for y in range(n):
        if check_boundary(x,y,1,0) and (castle_rooms[x][y].room_number != castle_rooms[x+1][y].room_number):
            max_area_withoutwall = max(max_area_withoutwall, area_group_size[castle_rooms[x][y].room_number-1] + area_group_size[castle_rooms[x+1][y].room_number-1])
        if check_boundary(x,y,0,1) and castle_rooms[x][y].room_number != castle_rooms[x][y+1].room_number:
            max_area_withoutwall = max(max_area_withoutwall, area_group_size[castle_rooms[x][y].room_number-1] + area_group_size[castle_rooms[x][y+1].room_number-1])
print(room_info.get_room_count())
print(max_area)
print(max_area_withoutwall)
f.close()