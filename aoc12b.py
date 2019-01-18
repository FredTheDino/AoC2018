def hash(grid, i):
    a = 0
    for n in range(i - 2, i + 3):
        a = (a << 1) | int(n in grid)
    return a

with open("input12.txt") as f:
    lines = f.readlines()
    grid = {}
    for i, c in enumerate(list(lines[0].split()[2])):
        if c == "#":
            grid[i] = "#" 
    
    rules = [0] * (2 ** 5)
    for line in lines[2:]:
        match = line.split()[0]

        a = 0
        for c in match:
            a = (a << 1) | int(c == "#")

        rules[a] = line.split()[2]

state = grid
next_state = {}
#for _ in range(50000000000 + 1):
for _ in range( 100000000 + 1):
    state = next_state
    next_state = {}
    for p in state:
        for i in range(p - 2, p + 3):
            if rules[hash(state, i)] == "#":
                next_state[i] = "#"

print(sum(state.keys()))
