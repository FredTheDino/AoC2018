bots = []
for line in open("input23"):
    splits = line.split(">, r=")
    r = int(splits[1])
    x, y, z = [int(x) for x in splits[0][5:].split(",")]
    bots.append((r, x, y, z))

def in_range(p, b2):
    dist = abs(p[0] - b2[1]) + abs(p[1] - b2[2]) + abs(p[2] - b2[3])
    return b2[0] >= dist

def intersects(b1, b2):
    dist = abs(b1[1] - b2[1]) + abs(b1[2] - b2[2]) + abs(b1[3] - b2[3])
    return (b2[0] + b1[0]) >= dist

def get_points(bot):
    points = set()
    for sign in [-1, 1]:
        points.add((bot[1] + sign * bot[0], bot[2], bot[3]))
        points.add((bot[1], bot[2] + sign * bot[0], bot[3]))
        points.add((bot[1], bot[2], bot[3] + sign * bot[0]))
    combined = set()
    for p in points:
        for t in points:
            x = (p[0] + t[0]) // 2
            y = (p[1] + t[1]) // 2
            z = (p[2] + t[2]) // 2
            combined.add((x, y, z))
    points.update(combined)
    return list(points)


def neighboring(point):
    x, y, z = point
    return [
        (x + 0, y + 0, z + 0),
        (x + 1, y + 0, z + 0),
        (x + 0, y + 1, z + 0),
        (x + 0, y + 0, z + 1),
        (x - 1, y - 0, z - 0),
        (x - 0, y - 1, z - 0),
        (x - 0, y - 0, z - 1)
    ]

bot = max(bots)
print(sum([in_range(b, bot) for b in bots]))
print(bots.index(min(bots)), min(bots))

best_count = 0
best_point = ()

for b in bots:
    for p in get_points(b):
        count = 0
        for s in bots:
            count += in_range(p, s)
        if count > best_count \
           or count == best_count and sum(p) < sum(best_point):
            best_point = p
            best_count = count

print("A")
                
# Search around the point
while True:
    new_count = 0
    new_best = ()
    for p in neighboring(best_point):
        count = 0
        for s in bots:
            count += in_range(p, s)

        if count > new_count:
            new_count = count
            new_best = p
    if sum(new_best) < sum(best_point):
        best_point = new_best
    break


print(best_point)
    
