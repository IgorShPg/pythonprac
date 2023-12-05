import asyncio
from time import strftime
async def main():
    task3 = asyncio.create_task(late(3, "Three"))
    task4 = asyncio.create_task(late(4, "Four"))
    await(task3)
    print(f"> {strftime('%X')}")
    await(task4)
    print(f"> {strftime('%X')}")


async def late(delay,name):
    print(f"start ({name})")
    await asyncio.sleep(delay)
    print(name)

    
asyncio.run(main()
