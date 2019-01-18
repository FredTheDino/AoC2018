

def print_cave(cave, units):
    for y, r in enumerate(cave):
        for x, c in enumerate(r):
            pos = (x, y)
            if pos in units:
                print(units[pos][1], end="")
            else:
                print(c, end="")
        print()

def attack(x, y, units, elfe_attack):
    if not (x, y) in units:
        print(x, y, "not a unit?")
        return
    adjacent = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    lowest_hp = 300
    lowest_pos = None
    for a in adjacent:
        if not a in units:
            continue
        if units[a][1] == units[(x, y)][1]:
            continue
        if units[a][0] < lowest_hp:
            lowest_hp = units[a][0]
            lowest_pos = a

    if lowest_pos is None:
        return
    target = units[lowest_pos]

    if units[(x, y)][1] == "E":
        attack_power = elfe_attack 
    else:
        attack_power = 3
    hp = target[0] - attack_power
    if hp <= 0:
        del units[lowest_pos]
    else:
        units[lowest_pos] = (hp, target[1], target[2])

def find_target(x, y, units, cave):
    d = 1
    if not (x, y) in units:
        return None
    this = units[(x, y)]
    adjacent = [(0, -1), (-1, 0), (+1, 0), (0, +1)]
    visited = {(x, y): 0}
    unvisited = [(x + a[0], y + a[1]) for a in adjacent]
    found = []
    while not found and unvisited:
        next_batch = []
        for x, y in unvisited:
            if (x, y) in visited:
                continue
            if cave[y][x] == "#":
                continue
            # Found something
            if (x, y) in units:
                unit = units[(x, y)]
                if unit[1] != this[1]:
                    found.append((x, y, d))
                continue
            visited[(x, y)] = d
            # Add to the node network
            # Branch out
            for dx, dy in adjacent:
                possible = (x + dx, y + dy)
                next_batch.append(possible)
        d += 1
        unvisited = next_batch
    # print(found)
    if found:
        found.sort(key=lambda p: p[1] * 200 + p[0]) 
        end = found[0]
        pos = (end[0], end[1])
        lowest_score = end[2]
        while True:
            next_pos = None
            for dx, dy in adjacent:
                guess = (pos[0] + dx, pos[1] + dy)
                if not guess in visited:
                    continue
                if visited[guess] == 0:
                    return pos
                if visited[guess] < lowest_score:
                    lowest_score = visited[guess]
                    next_pos = guess
            pos = next_pos
    return None
            

    
#for p in positions:
#    print(p, units[p])

def count(units):
    elves = 0
    goblins = 0
    for p in units:
        if units[p][1] == "G":
            goblins += 1
        else:
            elves += 1
    return elves, goblins


low = 3
high = 200

units = {}
cave = []
unit_id_counter = 0

done = False
while not done:
    units = {}
    cave = []
    unit_id_counter = 0
    for y, line in enumerate(open("input15.tt")):
        r = []
        for x, c in enumerate(line):
            if c in "#.":
                r.append(c)
            elif c in "GE":
                r.append(".")
                units[(x, y)] = (200, c, unit_id_counter)
                unit_id_counter += 1
        cave.append(r)
    start_elves, _ = count(units)
    elves_attack = (low + high) // 2
    turn = 0

    while True:
        positions = list(units.keys())
        positions.sort(key=lambda p: p[1] * 200 + p[0])
        turns_taken = set()

        for p in positions:
            if not p in units:
                continue
            this = units[p]
            if this[2] in turns_taken:
                continue
            turns_taken.add(this[2])
            new_pos = find_target(p[0], p[1], units, cave)
            if not new_pos:
                continue
            if not new_pos in units:
                # Move
                units[new_pos] = units[p]
                del units[p]
                p = new_pos
            # Attack
            attack(p[0], p[1], units, elves_attack)
            # print(p, "KILL", new_pos)
        elves, goblins = count(units)
        if elves < start_elves:
            low = elves_attack + 1
            print(elves_attack, "Goblins won", (low, high))
            break
        elif goblins == 0:
            print(elves_attack, "Elves won", (low, high))
            high = elves_attack
            if low == high:
                done = True
                break
            break
    
        turn += 1

accum = 0
# print_cave(cave, units)
for key in units.keys():
    #print(units[key][0])
    accum += units[key][0]

print(turn, accum)
print(turn * accum)
