from itertools import count
def r():
    s=0
    for i in count(1):
        yield (s:=s+1/i**2)

b=r()
print(next(b))
print(next(b))
print(next(b))

