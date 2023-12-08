import asyncio
from copy import copy
import sys
import random


async def merge(a,b,start,middle,finish,event_1in,event_2in,event_out):
    await asyncio.gather(event_1in.wait(),event_2in.wait())
    a,li1,li2=copy(a),start,middle
    for i in range(start,finish):
        if li2>=finish or li1<middle and a[li1]<a[li2]:
            b[i]=a[li1]
            li1+=1
        else:
            b[i]=a[li2]
            li2+=1
    event_out.set()


async def mtasks(a):
    s=copy(a)
    def fun(event_out,r1,r2):
        if r2-r1<=1:
            event_out.set()
            return list()
        event_1in=asyncio.Event()
        event_2in=asyncio.Event()
        return fun(event_1in,r1,(r1+r2)//2)+fun(event_2in,(r1+r2)//2,r2)+[merge(s,s,r1,(r1+r2)//2,r2,event_1in,event_2in,event_out)]
    return fun(asyncio.Event(),0,len(a)),s

exec(sys.stdin.read())
