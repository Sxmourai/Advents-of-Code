import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.read()

map = r.splitlines(keepends=False)
for y,row in enumerate(map):
    for x,char in enumerate(row):
        if char == "S":
            start_x,start_y = x,y


connections = {
    "S": {"left":True, "right":True, "up":True, "down":True},
    "F": {"left":False,"right":True, "up":False, "down":True},
    "-": {"left":True, "right":True, "up":False, "down":False},
    "7": {"left":True, "right":False, "up":False, "down":True},
    "L": {"left":False, "right":True, "up":True, "down":False},
    "|": {"left":False, "right":False, "up":True, "down":True},
    "J": {"left":True, "right":False, "up":True, "down":False},
}
sys.setrecursionlimit(100000)
def follow_loop(local_neighbors, start_x,start_y, perimeter=0):
    for dnx,dny in local_neighbors:
        nx = dnx+start_x
        ny = dny+start_y
        neighbor = map[ny][nx]
        print(perimeter, start_x,start_y, neighbor,local_neighbors, map[start_y][start_x])
        if perimeter>0 and neighbor=="S":
            return perimeter+1
        if neighbor not in connections.keys():continue
        if (dnx==1 and connections[neighbor]["left"]) or \
            (dnx==-1 and connections[neighbor]["right"]) or \
            (dny==1 and connections[neighbor]["up"]) or \
            (dny==-1 and connections[neighbor]["down"]):
            # print(nx,ny,neighbor)
            neighbor_neighbors=[]
            rel_pos = (-dnx, -dny)
            for pos in neighbors[neighbor]:
                if pos!=rel_pos:
                    neighbor_neighbors.append(pos)
            perimeter = follow_loop(neighbor_neighbors, nx,ny, perimeter=perimeter+1)
            if perimeter == None: # Found a broken loop
                continue
            else: return perimeter
    print(start_x, start_y)

neighbors = {
    "S": [(-1, 0),(0,-1),(0,1),(1,0)],
    "F": [(1, 0),(0,1),],
    "-": [(-1, 0),(1,0),],
    "7": [(-1, 0),(0,1),],
    "L": [(1, 0),(0,-1),],
    "|": [(0, -1),(0,1),],
    "J": [(-1, 0),(0,-1),],
}

print(follow_loop(neighbors["S"], start_x, start_y)) # 6599