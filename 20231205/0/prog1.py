import asyncio
from time import strftime

async def summa(x):
    return x+x
async def squarer(x):
    return x*x

async def main(*args):
    res=await asyncio.gather(*(squarer(arg) for arg in args))
    res=await asyncio.gather(*(summa(arg) for arg in res))
    print(*res)



    
