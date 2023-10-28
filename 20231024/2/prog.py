import itertools

def slide(seq,n):
    copy=seq
    while True:
        copy,seq=itertools.tee(copy)
        cur=list(itertools.islice(seq,n))
        if not cur:
            break
        yield from cur
        next(copy)
    










import sys
exec(sys.stdin.read())

