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
    operations = []
    events = []
    dlin=len(a)
    help=True
    count=1
    B=[0]*dlin
    C=[i for i in a]
    for i in range(dlin+1):
        events.append(asyncio.Event())
        events[i].set()
    dist=len(C)
    while count<dist:
        for i in range(0,dlin,count*2):
            z=i+count*2
            dlin2=len(C)
            end=min(z,dlin2)
            events.append(asyncio.Event())
            operations.append(asyncio.create_task(merge(C if help else B, B if help else C,i,min(i+count,dlin-1),end,events.pop(0),events.pop(0),events[-1])))
        events.append(events[-1])
        help=not help
        count*=2
    if help:
        return (operations,C)
    else:
        return (operations,B)
            
       



exec(sys.stdin.read())
