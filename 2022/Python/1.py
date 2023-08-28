i = open("1.txt").read().split("\n\n")


def first(i):
    r = []
    for e in i:
        r.append(sum(list(map(int, e.split()))))
    return r


def second(c):
    r = []
    for i in range(3):
        mc = max(c)
        r.append(mc)
        c.pop(c.index(mc))
    return r


c = first(i)
print(f"first: {max(c)}")
print(f"second: {sum(second(c))}")
