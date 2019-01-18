path = open("input20").readlines()[0].strip()
#path = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
#path = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
#path = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
#path = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
path = path[1:-1]

NORTH = 0b0001
WEST  = 0b0010
SOUTH = 0b0100
EAST  = 0b1000

rooms = {(0, 0): 0}
positions = [(0, 0)]

num_nodes = 0
class Node:
    def __init__(self, path):
        global num_nodes
        num_nodes += 1
        self.children = []
        if "(" in path:
            start = path.index("(")
            self.path = path[0:start]

            matching = start + 1
            counter = 1
            region_start = matching
            regions = []
            while matching < len(path):
                if path[matching] == "(":
                    counter += 1
                if path[matching] == "|" and counter == 1:
                    regions.append(path[region_start:matching])
                    region_start = matching + 1
                if path[matching] == ")":
                    counter -= 1
                    if counter == 0:
                        break
                matching += 1
            regions.append(path[region_start:matching])
            
            alts = regions
            for a in alts:
                self.children.append(Node(a))
            self.after = Node(path[matching+1:])
        else:
            self.path = path
            self.after = None


def get_flag(direction):
    if direction == "N":
        return NORTH, SOUTH
    if direction == "S":
        return SOUTH, NORTH
    if direction == "E":
        return EAST, WEST
    if direction == "W":
        return WEST, EAST

def move(rooms, pos, direction):
    flag_from, flag_to = get_flag(direction)
    rooms[pos] |= flag_from

    if direction == "N":
        pos = (pos[0], pos[1] - 1)
    if direction == "S":
        pos = (pos[0], pos[1] + 1)
    if direction == "E":
        pos = (pos[0] + 1, pos[1])
    if direction == "W":
        pos = (pos[0] - 1, pos[1])

    if not pos in rooms:
        rooms[pos] = 0
    rooms[pos] |= flag_to
    return pos

def print_map(rooms):
    low = (0, 0)
    high = (0, 0)
    for p in rooms:
        low  = (min(low[0],  p[0]), min(low[1],  p[1]))
        high = (max(high[0], p[0]), max(high[1], p[1]))

    for x in range((high[0] - low[0]) * 2 + 3):
        print("#", end="")
    print()

    for y in range(low[1], high[1] + 1):
        for x in range(low[0], high[0] + 1):
            if not (x, y) in rooms:
                print("##", end="")
            else: 
                if rooms[(x, y)] & WEST:
                    print("|", end="")
                else:
                    print("#", end="")
                if (x, y) == (0, 0):
                    print("X", end="")
                else:
                    print(".", end="")
        print("#")
        for x in range(low[0], high[0] + 1):
            if not (x, y) in rooms:
                print("##", end="")
            elif rooms[(x, y)] & SOUTH:
                print("#-", end="")
            else:
                print("##", end="")
        print("#")

def traverse(root, positions, rooms):
    for i, p in enumerate(positions):
        for c in root.path:
            p = move(rooms, p, c)       
        positions[i] = p
    new_positions = []
    for c in root.children:
        new_positions += traverse(c, positions[:], rooms)
    positions += new_positions
    positions = list(set(positions)) # This makes it a lot faster
    if root.after is not None:
        traverse(root.after, positions, rooms)
    return positions


def neighboring(pos, rooms):
    l = []
    doors = rooms[pos]
    if doors & NORTH:
        l.append((pos[0] + 0, pos[1] - 1))
    if doors & SOUTH:
        l.append((pos[0] + 0, pos[1] + 1))
    if doors & WEST:
        l.append((pos[0] - 1, pos[1] + 0))
    if doors & EAST:
        l.append((pos[0] + 1, pos[1] + 0))
    return l

def find_largest_distance(start, rooms):
    visited = {}
    distance = 0

    queue = [start]
    while queue:
        next_queue = []
        moved = False
        for p in queue:
            if p in visited:
                continue
            moved = True
            visited[p] = distance
            next_queue += neighboring(p, rooms)
		
        if not moved:
            break
        distance += 1	
        queue = next_queue

    return sum([visited[p] >= 1000 for p in visited])
    #return distance - 1

root = Node(path)
traverse(root, positions, rooms)
#print_map(rooms)
print(find_largest_distance((0, 0), rooms))
#print(
    
