def addr(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] + state[code[1]]
    return state

def addi(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] + code[1]
    return state

def mulr(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] * state[code[1]]
    return state

def muli(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] * code[1]
    return state

def banr(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] & state[code[1]]
    return state

def bani(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] & code[1]
    return state

def borr(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] | state[code[1]]
    return state

def bori(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] | code[1]
    return state

def setr(state, code):
    state = state[:]
    state[code[2]] = state[code[0]]
    return state

def seti(state, code):
    state = state[:]
    state[code[2]] = code[0]
    return state

def gtir(state, code):
    state = state[:]
    state[code[2]] = code[0] > state[code[1]]
    return state

def gtri(state, code):
    state = state[:]
    state[code[2]] = code[1] < state[code[0]]
    return state

def gtrr(state, code):
    state = state[:]
    state[code[2]] = state[code[1]] < state[code[0]]
    return state

def eqir(state, code):
    state = state[:]
    state[code[2]] = code[0] == state[code[1]]
    return state

def eqri(state, code):
    state = state[:]
    state[code[2]] = state[code[0]] == code[0] 
    return state

def eqrr(state, code):
    state = state[:]
    state[code[2]] = state[code[1]] == state[code[0]]
    return state

funcs = [
    addr, addi, mulr, muli, 
    banr, bani, borr, bori, 
    setr, seti, gtir, gtri, 
    gtrr, eqir, eqri, eqrr
]

lut = [
    "addr", "addi", "mulr", "muli", 
    "banr", "bani", "borr", "bori", 
    "setr", "seti", "gtir", "gtri", 
    "gtrr", "eqir", "eqri", "eqrr"
]

ip = 0
ops = []
state = [0, 0, 0, 0, 0, 0]
for line in open("input19"):
    if line[0] == "#":
        ip = int(line.split()[1])
    else:
        splits = line.split()
        f = funcs[lut.index(splits[0])]
        a, b, c = [int(x) for x in splits[1:]]
        ops.append((f, (a, b, c)))

while 0 <= state[ip] < len(ops):
    old = state
    op = ops[state[ip]]
    state = op[0](state, op[1])
    state[ip] = state[ip] + 1
    if old[0] != state[0]:
        print(state)

print(state)
