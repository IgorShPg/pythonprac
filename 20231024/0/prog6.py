from itertools import repeat

def repeater(n,seq):
    for i in range(len(seq)):
        yield from repeat(seq[i],n)

print(*list(repeater(5,"QEW")))
