# players = 10
# max_marble = 1618
# 
# players = 30
# max_marble = 5807
# 
# players = 9
# max_marble = 25

players = 459
max_marble = 72103 * 100

class Node:
    def __init__(self, v, p, n):
        self.value = v
        self.prev = p
        self.next = n

    def insert(self, v):
        n = Node(v, None, None)
        n.next = self.next
        n.prev = self
        self.next.prev = n
        self.next = n

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.value

def setup():
    a = Node(0, None, None)
    b = Node(1, a, a)
    a.next = b
    a.prev = b
    return a

def backup(l):
    for _ in range(6):
        l = l.prev
    return l

marbels = setup()
score = [0] * players

for m in range(2, max_marble + 1):
    if m % 100000 == 0:
        print(str(m / max_marble) + "%")
    if m % 23 == 0:
        marbels = backup(marbels)
        poped = marbels.pop()
        s = m + poped
        score[m % players] += s
    else:
        marbels = marbels.next.next
        marbels.insert(m)

print(max(score))
