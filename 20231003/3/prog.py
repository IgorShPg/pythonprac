from math import *

def Calc(s,t,u):
    x=lambda x:eval(s)
    y=lambda y:eval(t)
    w=lambda x,y:eval(u)
    return lambda t: w(x(t),y(t))








op,x=eval(input()),eval(input())
print(Calc(*op)(x))
