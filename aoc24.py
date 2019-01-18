groups = []
curr = None
for line in open("input24"):
    if "Immune System:" in line:
        curr = "IS"
        continue
    if "Infection:" in line:
        curr = "I"
        continue
    if line == "\n":
        continue

    weak = []
    imune = []

    if "(" in line:
        a, rest = line.split("(")
        w, b = rest.split(")")
        norm = a + b
        for s in w.split(";"):
            if "weak to" in s:
                weak = [x.strip() for x in s[8:].split(", ")]
            if "immune to" in s:
                imune = [x.strip() for x in s[10:].split(", ")]
    else:
        norm = line

    splits = norm.split()
    # side, num, hp, atk, type, initaive, weak:, imune:
    groups.append((curr, int(splits[0]), int(splits[4]), int(splits[12]), splits[13], int(splits[17]), weak, imune))

def is_done(groups):
    num_i  = sum(map(lambda g: g[0] == "I", groups))
    num_is = sum(map(lambda g: g[0] != "I", groups))
    return num_i == 0 or num_is == 0

def calculate_damage(g):
    def calc(target):
        if g[1] <= 0:
            return 0
        if g[0] == target[0]:
            return 0
        if g[4] in target[7]:
            return 0
        if g[4] in target[6]:
            bonus = 2
        else:
            bonus = 1
        return g[1] * g[3] * bonus
    return calc

def damage(g, damage):
    tmp = list(g)
    kills = min((damage // g[2]), tmp[1])
    tmp[1] -= kills
    return tuple(tmp), kills

#boost = 33
boost = 0
group_holder = groups[:]
while True:
    groups = group_holder[:]
    for i, g in enumerate(groups):
        if g[0] == "IS":
            g = list(g)
            g[3] += boost
            groups[i] = tuple(g)

    while not is_done(groups):
        groups.sort(key=lambda g: g[1] * g[3] + g[5] / 100, reverse=True)
        for g in groups:
            pass
            #print(g)
        targets = {} # Key is target, value is damage
        for i, g in enumerate(groups):
            damages = list(map(calculate_damage(g), groups))
            while True:
                dmg = max(damages) 
                if not dmg:
                    break
                target = damages.index(max(damages))
                if target in targets:
                    damages[target] = 0
                    continue
                targets[target] = (g[5], i, target) # dmg
                break
        
        attacks = list(targets.values())
        attacks.sort(reverse=True)
        total_kills = 0
        for _, attacker, target in attacks:
            dmg = calculate_damage(groups[attacker])(groups[target])
            groups[target], kills = damage(groups[target], dmg)
            total_kills += kills
        if total_kills == 0:
            break
        groups = list(filter(lambda g: g[1] > 0, groups))

    print("boost:", boost)
    infections = sum(map(lambda g: g[1] * (g[0] == "I"), groups))
    immunes = sum(map(lambda g: g[1] * (g[0] != "I"), groups))
    print("I", infections, "IS", immunes)
    if infections == 0:
        break
    
    boost += 1
print("done")
print(sum(map(lambda g: g[1], groups)))

