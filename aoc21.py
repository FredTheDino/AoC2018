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
    state[code[2]] = state[code[0]] == code[1] 
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

#ip = None
#ops = []
#state = [0, 0, 0, 0, 0, 0]
#for line in open("input21_pure"):
#    if line[0] == "#":
#        if ip is None:
#            ip = int(line.split()[1])
#    else:
#        splits = line.split()
#        f = funcs[lut.index(splits[0])]
#        a, b, c = [int(x) for x in splits[1:]]
#        ops.append((f, (a, b, c)))
#
#count = 0
#alts = []
#while 0 <= state[ip] < len(ops):
#    old = state
#    if state[ip] == 28:
#        count += 1
#        if not count % 10:
#            print(count)
#        alts.append(state[4])
#        if count == 100:
#            break
#    op = ops[state[ip]]
#    state = op[0](state, op[1])
#    state[ip] = state[ip] + 1
#
#print(alts)

alts = [103548, 4054948, 8744419, 13555206, 8399150, 16404615, 917647, 13023923, 2143665, 3671052, 13910700, 13335694, 2112144, 13520502, 14621494, 11506251, 5154057, 11895614, 7165053, 11445979, 15387181, 3784923, 6580645, 2179496, 2820429, 3812738, 11289445, 2239370, 720515, 14357681, 1660273, 16244372, 1748408, 9694215, 14216275, 9484345, 15295519, 14851013, 7079636, 8696498, 1664512, 2804794, 6809156, 12918112, 1153149, 11722123, 13798312, 5164845, 13955396, 8116045, 6082512, 16469495, 10902708, 11822262, 9193214, 7451632, 698487, 1037991, 13478177, 583828, 10188664, 5044673, 1228996, 13527118, 849160, 15672101, 2956608, 14497429, 4430789, 13313012, 16191825, 14341594, 12233781, 14683573, 4897840, 14109910, 639036, 3100168, 2591916, 9260878, 11686753, 9760336, 15583302, 344666, 7062280, 1908813, 9721927, 3174645, 5891307, 3325497, 10153771, 1571714, 5914935, 4201192, 10084670, 10628279, 4092243, 2920184, 11847142, 5152423]

def f(alts):
    answers = set()
    last = None
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    while True: # F
        r3 = r4 | 65536
        r4 = 10552971
        while True: # E
            r5 = r3 & 0xFF
            r4 = r4 + r5
            r4 = r4 & 0xFFFFFF
            r4 = r4 * 65899
            r4 = r4 & 0xFFFFFF
            r5 = 256 > r3
            if r5:
                if alts:
                    assert r4 == alts[0]
                if r4 in answers:
                    print(last)
                    return
                answers.add(r4)
                alts = alts[1:]
                last = r4
                break
            r3 = (r3) // 256

print(f(alts))

