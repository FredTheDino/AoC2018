depend = {} # A dict of sets
tasks = [] # A list of keys
for line in open("input7"):
    # A depends on B
    a = line.split()[7]
    if not a in tasks:
        tasks.append(a)
        depend[a] = set()

    b = line.split()[1]
    if not b in tasks:
        tasks.append(b)
        depend[b] = set()

    depend[a].add(b)

def time_of(a):
    return 60 + ord(a) - ord("A") + 1

tasks.sort()

time = 0 # The time accumulator. 
done = set() # All the finnished tasks.
curr = set() # All the current tasks.
workers = 5

while True:
    # If we don't have anything left to do, break.
    if not curr and not tasks:
        break
    # Loop through available tasks
    for a in filter(lambda x: not (depend[x] - done), tasks):
        # If noone can work. We can stop.
        print(a)
        if workers == 0:
            break
        print(a, time)
        workers -= 1
        curr.add((time + time_of(a), a))
        del tasks[tasks.index(a)]

    # Complete the next task.
    c = min(curr)
    print(c[1], c[0])
    curr.remove(min(curr))
    done.add(c[1])
    assert(time <= c[0])
    time = c[0]
    workers += 1

print(time)

