grid = {}
for y, line in enumerate(open("input18_full")):
    for x, c in enumerate(line.strip()):
        grid[(x, y)] = c

def adjacent(x, y):
    result = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
    result.remove((x, y))
    return result

def print_grid(grid):
    print("================")
    max_corner = max(grid.keys())
    for y in range(max_corner[1] + 1):
        for x in range(max_corner[0] + 1):
            print(grid[(x, y)], end="")
        print("")

def hash(grid):
    yard, tree = 0, 0
    max_corner = max(grid.keys())
    for x in range(max_corner[0] + 1):
        for y in range(max_corner[1] + 1):
            if grid[(x, y)] == "|":
                tree += 1
            elif grid[(x, y)] == "#":
                yard += 1
    return yard, tree

max_corner = max(grid.keys())
hashes = []
for i in range(750):
    next_grid = grid.copy()
    for x in range(max_corner[0] + 1):
        for y in range(max_corner[1] + 1):
            ad = adjacent(x, y)
            num_tree = 0
            num_yard = 0
            for a in ad:
                if a in grid:
                    if grid[a] == "|":
                        num_tree += 1
                    elif grid[a] == "#":
                        num_yard += 1
            state = grid[(x, y)]
            if state == "#":
                if num_tree == 0 or num_yard == 0:
                    next_grid[(x, y)] = "."
            elif state == "|":
                if num_yard >= 3:
                    next_grid[(x, y)] = "#"
            elif state == ".":
                if num_tree >= 3:
                    next_grid[(x, y)] = "|"
    hashes.append((i, hash(grid)))
    grid = next_grid
hashes.append((i + 1, hash(grid)))

for i, h in hashes[-100:]:
    print(i, h[0] * h[1])

yard, tree = hash(grid)
print(yard, tree, yard * tree)

