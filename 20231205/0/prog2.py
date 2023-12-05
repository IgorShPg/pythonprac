import asyncio


async def send(evsnd):
    evsnd.set()
    print("snd sent", evsnd)

async def mid(evsnd,evmid):
    await evsnd.wait()
    print("mid got", evsnd)
    evmid.get()
    print("mid sent", evmid)

async def recv(evmid1,evmid2):
    await evmid1.wait()
    print("recv got", evmid1)
    await evmid2.wait()
    print("recv got", evmid2)

class Ev(asyncio.Event):
    def __init__(self,name):
        self.name=name
        super().__init__()
    def __str__(self):
        return f"<{self.name}>"

async def main():
    es, em1, em2=(Ev(name) for name in ("evsnd", "evmid1", "evmid2"))
    await asyncio.gather(
        send(evsnd),
        mid(evsnd,evmid1),
        mid(evsnd,evmid2),
        recv(evmid1,evmid2))

asyncio.run(main())

