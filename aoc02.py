
def diff(line_a, line_b):
    differences = 0
    for a, b in zip(line_a, line_b):
        if a != b:
            differences += 1
    return differences

with open("input2.txt") as file:
    lines = file.readlines()
    for i, a in enumerate(lines):
        for b in lines[(i + 1):]:
            if diff(a, b) == 1:
                print(a, "\n", b)
                break

