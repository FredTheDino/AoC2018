def parse_array(line):
    after = line.split(maxsplit=1)[1].strip()
    state = {}
    exec("data = " + after, state)
    return state["data"]

lines = open("input16").readlines()
operations = []
for i in range(0, len(lines), 4):
    code   = [int(x) for x in lines[i + 1].split()]
    before = parse_array(lines[i + 0])
    after  = parse_array(lines[i + 2])
    operations.append((code, before, after))

def addr(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] + state[code[2]]
    return state

def addi(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] + code[2]
    return state

def mulr(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] * state[code[2]]
    return state

def muli(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] * code[2]
    return state

def banr(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] & state[code[2]]
    return state

def bani(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] & code[2]
    return state

def borr(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] | state[code[2]]
    return state

def bori(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] | code[2]
    return state

def setr(state, code):
    state = state[:]
    state[code[3]] = state[code[1]]
    return state

def seti(state, code):
    state = state[:]
    state[code[3]] = code[1]
    return state

def gtir(state, code):
    state = state[:]
    state[code[3]] = code[1] > state[code[2]]
    return state

def gtri(state, code):
    state = state[:]
    state[code[3]] = code[2] < state[code[1]]
    return state

def gtrr(state, code):
    state = state[:]
    state[code[3]] = state[code[2]] < state[code[1]]
    return state

def eqir(state, code):
    state = state[:]
    state[code[3]] = code[1] == state[code[2]]
    return state

def eqri(state, code):
    state = state[:]
    state[code[3]] = state[code[1]] == code[2] 
    return state

def eqrr(state, code):
    state = state[:]
    state[code[3]] = state[code[2]] == state[code[1]]
    return state

funcs = [
        addr, addi, mulr, muli, 
        banr, bani, borr, bori, 
        setr, seti, gtir, gtri, 
        gtrr, eqir, eqri, eqrr
    ]

if __name__ == "__main__":
    # Map op-codes to potential functions
    ops = [set(range(0, 16)) for _ in range(len(funcs))]

    for op in operations:
        opcode = op[0][0]
        for e, f in enumerate(funcs):
            if not e in ops[opcode]:
                continue
            if f(op[1], op[0]) != op[2]:
                ops[opcode].remove(e)

    for _ in funcs:
        for options in ops:
            if len(options) != 1:
                continue
            for code, o in enumerate(ops):
                if o == options:
                    continue
                ops[code] -= options

    state = [0, 0, 0, 0]
    ops = [funcs[list(o)[0]] for o in ops]
    for line in open("input16b"):
        code = [int(i) for i in line.split()]
        state = ops[code[0]](state, code)
    print(state)
    print(state[0])




