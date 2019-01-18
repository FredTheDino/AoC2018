
grid = {}

def get_power_level(x, y):
    rackID = x + 10
    power = rackID * y
    power += 5535
    return ((power // 100) % 10) - 5


for x in range(1, 301):
    for y in range(1, 301):
        grid[(x, y)] = get_power_level(x, y)

def get_power_sum(x, y, d):
    return sum([grid[(x + a, y + b)] for a in range(d) for b in range(d)])

best = -100
cord = None
for d in range(3, 4):
    for x in range(1, 300 - d):
        for y in range(1, 300 - d):
            power = get_power_sum(x, y, d)
            if power > best:
                cord = (x, y, d)
                best = power

print(cord, power)

