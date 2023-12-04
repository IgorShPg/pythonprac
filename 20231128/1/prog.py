import sys
import types


def helpach(fun):
    def new_fun(self,*args,**kwargs):
        print('{}: {}, {}'.format(fun.__name__, args, kwargs))
        return fun(self,*args, **kwargs)
    return new_fun

class dump(type):
    def __new__(cls,name,base,attr):
        newf={}
        for name, fun in attr.items():
            if isinstance(fun,types.FunctionType):
                fun=helpach(fun)
            newf[name]=fun
        attr=newf
        return super().__new__(cls,name,base,attr)
        


exec(sys.stdin.read())




