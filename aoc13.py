
track = {}
carts = {}

for y, line in enumerate(open("input13.txt")):
    for x, c in enumerate(line):
        if c == " ":
            continue
        if c == ">" or c == "<":
            track[(x, y)] = "-"
            carts[(x, y)] = (c, 0)
        elif c == "^" or c == "v":
            track[(x, y)] = "|"
            carts[(x, y)] = (c, 0)
        else:
            track[(x, y)] = c

def move(pos, cart, track):
    piece = track[pos]
    d = cart[0]
    if piece == "\\":
        if   d == ">": d = "v"
        elif d == "<": d = "^"
        elif d == "v": d = ">"
        elif d == "^": d = "<"
    elif piece == "/":
        if   d == ">": d = "^"
        elif d == "<": d = "v"
        elif d == "v": d = "<"
        elif d == "^": d = ">"
    elif piece == "+":
        rots = ["<", "^", ">", "v"]
        d = rots[(rots.index(cart[0]) + cart[1] - 1) % len(rots)]
        cart = (d, (cart[1] + 1) % 3)

    if d == "<": pos = (pos[0] - 1, pos[1])
    if d == ">": pos = (pos[0] + 1, pos[1])
    if d == "^": pos = (pos[0], pos[1] - 1)
    if d == "v": pos = (pos[0], pos[1] + 1)

    return pos, (d, cart[1])


something = 0
while True:
    positions = list(carts.keys())
    if something != len(positions):
        something = len(positions)
        print(positions)
        print(something)
    if len(positions) == 1:
        print(positions)
        break
    positions.sort(key=lambda a: (a[1], a[0]))
    for pos in positions:
        if not pos in carts:
            continue

        new_pos, cart = move(pos, carts[pos], track)
        del carts[pos]
        if new_pos in carts:
            del carts[new_pos]
            continue
        carts[new_pos] = cart



