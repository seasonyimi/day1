#-*-coding:utf8-*-
#asyncio  消息循环，从模板中直接获取一个EventLoop引用，然后把协程丢到EventLoop中执行，就实现了异步IO
import asyncio
import aiohttp
import aiohttp

async def hell0():
    print("Hello world")
    #异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print("Hello again")

# 获取EventLoop
loop = asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hell0())
loop.close()

