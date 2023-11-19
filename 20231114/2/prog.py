import sys

class Num:
    num=0
    def __init__(self):
        self.num=0
    def __set__(self,obj,val):
        if hasattr(val,"real"):
            obj.__dict__["num"]=val
        else:
            obj.__dict__["num"]=len(val)
    def __get__(self,obj,t):
        if "num" in obj.__dict__:
            return obj.__dict__["num"]
        else:
            return self.__dict__["num"]
        
exec(sys.stdin.read())
