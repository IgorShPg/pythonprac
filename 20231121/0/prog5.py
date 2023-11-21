
import pickle

class SerCls:
    def __init__(self,ls,dc,nu,s):
        self.lst=ls
        self.dct=dc
        self.num=nu
        self.st=s

ser=SerCls([1,2,3],{'sk':1,'djjd':4},34,"kdkkdkd")

res=pickle.dumps(ser)
del ser
ser1=pickle.loads(res)
print(ser1.dct)
