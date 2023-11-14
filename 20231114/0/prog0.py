from functools import wraps


def debug(fun):
    def wrapper(*args):
        print("<",*args)
        res=fun(*args)
        print(">",res)
        return res
    return wrapper

@debug
def mult(a, b):
    return a*b

print(mult(11,4))
    
