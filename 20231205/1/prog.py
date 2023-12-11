import asyncio
import sys

event = asyncio.Event()
ev1=asyncio.Event()
ev2=asyncio.Event()

async def writer(queue, delay):
    i = 0
    while not event.is_set():
        await asyncio.sleep(delay)
        await queue.put(f"{i}_{delay}")
        i += 1
   
       


async def stacker(queue, stack):
    while not event.is_set():
        await stack.put(await queue.get())



async def reader(stack, num, delay):
    i=0
    while not event.is_set():
        await asyncio.sleep(delay)
        elem = await stack.get()
        print(elem)
        i += 1
        if i == num:
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

