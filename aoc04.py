guards = {}

with open("input4") as f:
    data = []
    for line in f.readlines():
        splits = line.split()
        date = tuple([int(i) for i in splits[0][1:].split("-")])
        time = tuple([int(i) for i in splits[1][:-1].split(":")])
        task = splits[3]
        data.append((date, time, task))
    data.sort()
    
    current_guard = None
    asleep = 0
    for d in data:
        if d[2][0] == "#":
            # Change guard
            current_guard = d[2]
            if not current_guard in guards:
                guards[current_guard] = [0] * 60
        elif d[2][0] == "a":
            # Asleep
            asleep = d[1][1]
        else:
            # Wakeup
            wakeup_time = d[1][1]
            for i in range(asleep, wakeup_time):
                guards[current_guard][i] += 1

    most_asleep_name = ""
    most_asleep_time = 0
    for g in guards:
        t = max(guards[g])
        if t > most_asleep_time:
            most_asleep_time = t
            most_asleep_name = g

    time = guards[most_asleep_name]
    print(time.index(most_asleep_time) * int(most_asleep_name[1:]))








