depth = 3558
target = (15, 740)

#depth = 510
#target = (10, 10)
r = 50

area = (target[0] + r, target[1] + r)

def calculate_errosion(area, target, depth):
    el = {}
    for x in range(1, area[0] + 1):
        el[(x, 0)] = (x * 16807 + depth) % 20183
    for y in range(1, area[1] + 1):
        el[(0, y)] = (y * 48271 + depth) % 20183
    for x in range(1, area[0] + 1):
        for y in range(1, area[1] + 1):
            el[(x, y)] = (el[(x-1, y)] * el[(x, y-1)] + depth) % 20183
    el[(0, 0)] = depth % 20183
    el[target] = depth % 20183

    for p in el:
        el[p] %= 3

    return el

el = calculate_errosion(area, target, depth)

def neighbor(field, x, y, t):
    neighbor = [(x + 1, y + 0, t),
                (x + 0, y - 1, t),
                (x + 0, y + 1, t),
                (x - 1, y + 0, t)]

    for n in [0, 1, 2]:
        if n == t or n == field[(x, y)]:
            continue
        neighbor.append((x, y, n))

    neighbor = list(filter(lambda n: (n[0], n[1]) in field and field[(n[0], n[1])] != n[2], neighbor))
    return neighbor

def pathfind(field, sink):
    source = (0, 0, 1)
    weights = {source: 0}
    queue = set([source])
    path = {}
    visited = set()

    while queue:
        w, p = min([(weights[p], p) for p in queue])
        x, y, t = p
        queue.remove(p)
        visited.add(p)

        for n in neighbor(field, x, y, t):
            if t != n[2]:
                v = w + 7
            else:
                v = w + 1

            if not n in weights or v < weights[n]:
                path[n] = (x, y, t)
                weights[n] = v
                if n == sink:
                    break
                if not n in visited:
                    queue.add(n)

    return weights[sink]

print(pathfind(el, (target[0], target[1], 1)))




