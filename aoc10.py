
points = []
for line in open("input10"):
    pos = tuple([int(x) for x in line.split()[:2]])
    vel = tuple([int(x) for x in line.split()[2:]])
    points.append((pos, vel))

def find_bounding_box(points, t):
    min_pos = (10000, 10000)
    max_pos = (0, 0)
    for p in points:
        x = p[0][0] + p[1][0] * t
        y = p[0][1] + p[1][1] * t
        min_pos = (
                min(min_pos[0], x),
                min(min_pos[1], y),
            )
        max_pos = (
                max(max_pos[0], x),
                max(max_pos[1], y),
            )

    return (min_pos, max_pos)

def find_bounding_box_area(points, t):
    min_pos, max_pos = find_bounding_box(points, t)
    return (max_pos[0] - min_pos[0]) * (max_pos[1] - min_pos[1])

def print_points(points, t):
    box = find_bounding_box(points, t)
    final = [(p[0][0] + p[1][0] * t, p[0][1] + p[1][1] * t) for p in points]
    width  = box[1][0] - box[0][0]
    height = box[1][1] - box[0][1]
    grid = {}
    for p in final:
        grid[(p[0] - box[0][0], p[1] - box[0][1])] = "#"

    for y in range(height + 1):
        for x in range(width + 1):
            pos = (x, y)
            if pos in grid:
                print("#", end="")
            else:
                print(" ", end="")
        print("")

l = 0
low = (find_bounding_box_area(points, l), l)
h = 20000
high = (find_bounding_box_area(points, h), h)
t = 0
while True:
    if abs(low[1] - high[1]) <= 1:
        t = min(low, high)[1]
        break

    g = (low[1] + high[1]) // 2
    guess = (find_bounding_box_area(points, g), g)

    smallest = [guess, low, high]
    smallest.sort()
    smallest = smallest[:2]
    low, high = smallest

print_points(points, t)
print(t)


