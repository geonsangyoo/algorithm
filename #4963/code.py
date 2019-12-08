import sys

# Constants
LAND = 1
SEA = 0
PASSED = 9
DEBUG = True
SEARCH_ARRAY = [-1, 0, 1]
#DEBUG = False

# Global variables
count = 0

# Chart 8 directions based on x,y coordinate
def chart(x, y, count):
    check_nodes = list()
    if land_map[x][y] == LAND:
        # Initial insertion
        check_nodes.append([x, y])
        land_map[x][y] = PASSED
        # Search over 8 directions until node list becomes empty
        while len(check_nodes) > 0:
            # Assign new a coordinate from node list
            x, y = check_nodes.pop()
            for d1 in SEARCH_ARRAY:
                for d2 in SEARCH_ARRAY:
                    if ((x + d1 >= 0) & (x + d1 < height)) & ((y + d2 >= 0) & (y + d2 < width)):
                        if land_map[x + d1][y + d2] == LAND:
                            land_map[x + d1][y + d2] = PASSED
                            check_nodes.append([x + d1, y + d2])
        count = count + 1
    return count

# Load data from input.txt
if DEBUG: 
    f = open("/Users/yoogeonsang/Documents/python/algorithm/#4963/input.txt")
else:
    f = sys.stdin

while True:
    width, height = map(int, f.readline().split())
    if width <= 0 & height <= 0: # Terminate PGM
        break

    # Assign elements in current order
    count = 0
    land_map = [list(map(int, f.readline().split())) for _ in range(0, height)]
    
    # Fan out to all territory
    for h in range(0, height):
        for w in range(0, width):
            count = chart(h, w, count)

    # Print out final count
    print(count)

# Close the file object
f.close()