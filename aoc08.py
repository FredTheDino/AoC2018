

data = []
i = 0
with open("input8") as f:
    data = [int(x) for x in f.readlines()[0].split()]
    
    

def read_node():
    global data, i
    num_children = data[i]
    num_meta = data[i+1]
    i += 2
    children = []
    for _ in range(num_children):
        children.append(read_node())

    meta = []
    for _ in range(num_meta):
        meta.append(data[i])
        i += 1
    return (meta, children)

def summer(node):
    if len(node[1]) != 0:
        s = 0
        for n in node[0]:
            n -= 1
            if len(node[1]) <= n:
                continue
            s += summer(node[1][n])
        return s
    else:
        return sum(node[0])

root = read_node()
print(summer(root))
