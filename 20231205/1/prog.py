import asyncio
import sys

event = asyncio.Event()
ev1=asyncio.Event()
ev2=asyncio.Event()

async def writer(queue, delay):
    i = 0
    await asyncio.sleep(delay)
    while not event.is_set():
        #await asyncio.sleep(delay)
        await queue.put(f"{i}_{delay}")
        i += 1
        await asyncio.sleep(delay)
   
       


async def stacker(queue, stack):
    while not event.is_set():
        await stack.put(await queue.get())



async def reader(stack, num, delay):
    for i in range(num):
        #await asyncio.sleep(delay)
        print(await stack.get())
        await asyncio.sleep(delay)
    event.set()


async def main():
    a, b, c, n = eval(input())
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    await asyncio.gather(
        writer(queue,a),
        writer(queue,b),
        stacker(queue,stack),
        reader(stack,n,c)
    )
    

asyncio.run(main())

