lower_chars = "abcdefghijklmnopqrstuvwxyz"
upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
polys = zip(lower_chars, upper_chars)


import sys
with open("input5") as f:
    original = f.read().strip()

    best = len(original)
    for c1, c2 in polys:
        print(".", end="")
        sys.stdout.flush()
        polymer = list(original.replace(c1, "").replace(c2, ""))
        while True:
            found = False
            i = 0
            while i < len(polymer) - 1:
                a = polymer[i]
                b = polymer[i + 1]
                if a != b and a.lower() == b.lower():
                    del polymer[i]
                    del polymer[i]
                    found = True
                    continue
                i += 1
            if not found:
                break
        best = min(len(polymer), best)
    print()
    print(best)
