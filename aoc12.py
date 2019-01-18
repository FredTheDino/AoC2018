def hash(l, i):
    a = ""
    for n in range(i - 2, i + 3):
        a += l[n]
    return a

with open("input12.txt") as f:
    lines = f.readlines()
    start = -100
    inital_state = list("." * abs(start) + lines[0].split()[2] + "." * abs(200))

    rules = {}
    for line in lines[2:]:
        match = line.split()[0]
        rules[hash(match, 2)] = line.split()[2]

print(inital_state)

for k in rules:
    print(k, "=>", rules[k])

def find(state, reverse=True):
    if reverse:
        for i, x in enumerate(reversed(state)):
            if x == "#":
                return len(state) - i
    for i, x in enumerate(state):
        if x == "#":
            return i


state = inital_state
next_state = inital_state[:]
for c in range(95):
    state, next_state = next_state, state
    print("".join(state[find(state, False):find(state, True)]))
    for i in range(2, len(state) - 2):
        next_state[i] = rules[hash(state, i)]

accum = 0
for i, p in enumerate(state):
    if p == "#":
        accum += i + start + 50000000000 - c
print(accum)
