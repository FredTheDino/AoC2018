import sys

def time_of_task(t):
    return 60 + ord(t) - ord("A") + 1

with open("input7") as f:
    depend = {}
    todo = set()
    for line in f.readlines():
        splits = line.split()
        a = splits[7]
        b = splits[1]
        if not a in todo:
            todo.add(a)
            depend[a] = set()
        if not b in todo:
            todo.add(b)
            depend[b] = set()
        if a in todo:
            depend[a].add(b)

    done = set()
    tasks = list(todo)
    tasks.sort()

    num_elfs = 5
    doing = []
    time = 0
    while True:
        if not (tasks or doing):
            break

        for i, t in enumerate(tasks):
            if (depend[t] - done) or num_elfs == 0: continue
            print("started:", t, time)
            num_elfs -= 1
            doing.append((t, time_of_task(t)))
            del tasks[i]
        for i, task in enumerate(doing):
            if task[1] == 1:
                num_elfs += 1
                done.add(task[0])
                del doing[i]
            else:
                doing[i] = (task[0], task[1] - 1)
        for i, t in enumerate(tasks):
            if (depend[t] - done) or num_elfs == 0: continue
            print("finished:", t, time)
            num_elfs -= 1
            doing.append((t, time_of_task(t)))
            del tasks[i]
        time += 1

    print(time)
