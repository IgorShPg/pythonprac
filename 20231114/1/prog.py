import sys


def objcount(cls):
    class count(cls):
        cls.counter=0
        def __init__(self,*args,**kwargs):
            cls.counter+=1
        def __del__(self,*args,**kwargs):
            cls.counter-=1
    return count

exec(sys.stdin.read())
