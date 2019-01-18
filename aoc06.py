from PIL import Image, ImageDraw
from random import randint

def manhattan(x, y, a, b):
    return abs(x - a) + abs(y - b)

def is_edge(x, y, min_pos, max_pos):
    return x == min_pos[0] or y == min_pos[1] or \
           x == (max_pos[0] - 1) or y == (max_pos[1] - 1)

with open("input6") as f:
    positions = [[int(y) for y in x.split(", ")] for x in f.readlines()]
    max_pos = positions[0]
    for x, y in positions:
        max_pos = (max(x + 40, max_pos[0]), max(y + 40, max_pos[1]))
    dim = max_pos

    grid = [[0 for i in range(dim[1])] for _ in range(dim[0])]
    for x in range(dim[0]):
        for y in range(dim[1]):
            accum = 0
            for p in positions:
                accum += manhattan(x, y, p[0], p[1])
            grid[x][y] = accum < 10000

    summer = 0
    for a in grid:
        for b in a:
            summer += b
    print(summer)
#    dim = max_pos
#
#    print(dim)
#    print("Area:", dim[0] * dim[1])
#    
#    dists = [0 for p in positions]
#    grid = [[-1 for i in range(dim[1])] for _ in range(dim[0])]
#    for x in range(dim[0]):
#        for y in range(dim[1]):
#            closest = -1
#            distance = -1
#            for i, p in enumerate(positions):
#                d = manhattan(x, y, p[0], p[1])
#                if d == distance:
#                    closest = -1
#                elif d < distance or distance == -1:
#                    distance = d
#                    closest = i
#            grid[x][y] = closest
#            if closest != -1:
#                dists[closest] += distance
#
#
#    accum = [0 for p in positions]
#    for x in range(dim[0]):
#        for y in range(dim[1]):
#            if grid[x][y] == -1: continue
#            if is_edge(x, y, (0, 0), dim):
#                accum[grid[x][y]] = -1
#            if accum[grid[x][y]] == -1:
#                continue
#            accum[grid[x][y]] += 1
#
#    print("Largest region:", max(accum))

