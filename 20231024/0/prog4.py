def travel(n):
    while n:
        yield "по кочкам\n"
        n-=1
    return "и в яму"

def travelwrap(n):
    res=yield from travel(n)
    yield res


print(*list(travelwrap(5)))
