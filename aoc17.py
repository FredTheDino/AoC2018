clay = {}
area = (1000, 1000, 0, 0)
for line in open("input17"):
    splits = line.split(", ")
    if splits[0][0] == "x":
        low_x = int(splits[0][2:])
        high_x = low_x + 1
        splits = splits[1].split("..")
        low_y = int(splits[0][2:])
        high_y = int(splits[1]) + 1
    else:
        low_y = int(splits[0][2:])
        high_y = low_y + 1
        splits = splits[1].split("..")
        low_x = int(splits[0][2:])
        high_x = int(splits[1]) + 1
    area = (
        min(low_x, area[0]), 
        min(low_y, area[1]), 
        max(high_x, area[2]), 
        max(high_y, area[3])
    )
    for x in range(low_x, high_x):
        for y in range(low_y, high_y):
            clay[(x, y)] = "#"

#clay[(500, 0)] = "+"
def print_world(area, clay, water):
    for x in range(area[0] - 1, area[2] + 1):
        print("=", end="")
    print()
    for y in range(area[1], area[3]):
        for x in range(area[0] - 1, area[2] + 1):
            if (x, y) in clay:
                print(clay[(x, y)], end="")
            elif (x, y) in water:
                print(water[(x, y)], end="")
            else:
                print(" ", end="")
        print("")


def print_around(point, clay, water, r=15):
    area = (point[0] - r, point[1] - r, point[0] + r, point[1] + r)
    print_world(area, clay, water)


def is_solid(point, clay, water):
    return point in clay or (point in water and water[point] == "~")


def fill(source, area, clay, water):
    # Going down
    #print_world(area, clay, water)
    #print(source) 
    #print(source)
    while True:
        depth = 0
        floor = None
        while (source[1] + depth) <= area[3]:
            drip_pos = (source[0], source[1] + depth)
            if is_solid(drip_pos, clay, water):
                depth -= 1
                floor = (source[0], source[1] + depth)
                break
            else:
                depth += 1
                water[drip_pos] = "|"

        if floor is None or floor[1] == source[1]:
            return
        last = floor
        sources = []
        # Go right
        for direction in [-1, 1]:
            offset = 0
            while True:
                pos =   (floor[0] + direction * offset, floor[1] + 0)
                under = (floor[0] + direction * offset, floor[1] + 1)
                if is_solid(pos, clay, water):
                    break
                if not is_solid(under, clay, water):
                    sources.append(pos)
                    break
                offset += 1

        fill_symbol = "~" if not sources else "|"
        filled = 0
        if not floor in water or water[floor] != fill_symbol:
            filled += 1
            water[floor] = fill_symbol

        for direction in [-1, 1]:
            offset = 1
            while True:
                pos   = (floor[0] + direction * offset, floor[1] + 0)
                under = (floor[0] + direction * offset, floor[1] + 1)
                if is_solid(pos, clay, water):
                    break
                if not pos in water or water[pos] != fill_symbol:
                    filled += 1
                    water[pos] = fill_symbol
                offset += 1
                if not is_solid(under, clay, water):
                    break

        #print_around(floor, clay, water)
        #print(sources, filled)
        if not filled:
            return

        depth -= 1
        if sources:
            for s in sources:
                fill(s, area, clay, water)
        #print_around(floor, clay, water)
    
source = (500, 0)
water = {}
fill(source, area, clay, water)
#print_world(area, clay, water)

print("all:", sum([(area[1] <= y < area[3]) for _, y in water]))
print("flowing:", sum([(area[1] <= y < area[3] and water[(x, y)] == "|") for x, y in water]))
