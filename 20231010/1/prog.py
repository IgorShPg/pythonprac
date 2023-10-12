from fractions import Fraction
from math import *


def help(s,cof):
    sum=0
    deg=len(cof)-1
    for i in cof:
        sum+=i*s**deg
        deg-=1
    return sum
    



def sol(*par):
    s,w=Fraction(par[0]),Fraction(par[1])
    degA=par[2]
    first=[Fraction(i) for i in par[3:3+degA+1]]
    degB=par[3+degA+1]
    second=[Fraction(i) for i in par[4+degA+1:]]
    pol1=help(s,first)
    pol2=help(s,second)
    if pol2==0:
        return False
    else:
        return (pol1/pol2)==w

  
print(sol(*eval(input())))
