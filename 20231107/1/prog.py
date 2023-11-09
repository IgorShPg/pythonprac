import collections
import sys


class DivStr(collections.UserString):
    def __init__(self,str=""):
        super().__init__(str)
    def __mod__(self,number):
        size=len(self)%number
        return self[-size:]
    def __floordiv__(self,number):
        size=len(self)//number
        return iter(self[i:i+size] for i in range(0,number*size,size))
    

exec(sys.stdin.read())
