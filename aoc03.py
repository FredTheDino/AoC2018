fabric_squares = {}

with open("input03") as f:
    data = []
    for line in f.readlines():
        splits = line.split()
        x, y = [int(x) for x in splits[2][:-1].split(",")]
        w, h = [int(x) for x in splits[3].split("x")]
        data.append((x, y, w, h))

    for x, y, w, h in data:
        for x_pos in range(x, x + w):
            for y_pos in range(y, y + h):
                key = (x_pos, y_pos)
                if key in fabric_squares:
                    fabric_squares[key] += 1
                else:
                    fabric_squares[key] = 1

    for x, y, w, h in data:
        for x_pos in range(x, x + w):
            for y_pos in range(y, y + h):
                key = (x_pos, y_pos)
                if fabric_squares[key] > 1:
                    correct = False
                    break
            if not correct:
                break
        if correct:
            print(i)





