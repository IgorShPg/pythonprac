

def fib(m,n):
    a=1
    b=1
    i=0
    while i<m:
        a,b=b,b+a
        i+=1
    i=1
    while i<=n:
        yield a
        a,b=b,b+a
        i+=1

import sys
exec(sys.stdin.read())
