points = []
for line in open("input25"):
    points.append(tuple([int(x) for x in line.split(",")]))

def in_range(p1, p2):
    return sum([abs(a - b) for a, b in zip(p1, p2)]) <= 3

points.sort()

constilations = []
for a in points:
    found = False
    for c in constilations:
        for b in c:
            if in_range(a, b):
                c.append(a)
                found = True
                break
        if found:
            break
    if not found:
        constilations.append([a])

did_something = True
while did_something:
    did_something = False
    i = 0
    while i < len(constilations):
        j = i + 1
        while j < len(constilations):
            c1 = constilations[i]
            c2 = constilations[j]
            for a in c1:
                for b in c2:
                    if in_range(a, b):
                        constilations[i] += c2
                        del constilations[j]
                        j = j - 1
                        did_something = True
                        break
                else:
                    continue
                break
            j = j + 1
        i = i + 1

print(len(constilations))
