
def factor(n):
    l = []
    c = 0
    while not n % 2:
        c += 1
        n //= 2
    if c: l.append((2, c))
    i = 3
    while i * i <= n:
        c = 0
        while not n % i:
            c += 1
            n //= i
        if c: l.append((i, c))
        i += 2
    if n != 1: l.append((n, 1))
    return l

def div_sum(factors, i=0, n=1):
    if i == len(factors):
        return n
    s = 0
    f, c = factors[i]
    for _ in range(c + 1):
        s += div_sum(factors, i + 1, n)
        n *= f
    return s

print(div_sum(factor(10551428)))

#
#n = 10551428
#c = 0 # r0
#a = 1
#while True:
#    if not n % a:
#        print(a, n // a)
#        c += a
#    a += 1
#    if a > n:
#        break
#print(c)
