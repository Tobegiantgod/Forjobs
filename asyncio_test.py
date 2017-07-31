#coding: utf-8
"""
    使用asyncio通过异步实现并发(异步通过协程实现，协程通过生成器实现），如下可以看到，当使用异步模式的时候
(每次使用调用asyncio.sleep(1)),进程控制权会返回到主程序的消息循环里，并开始运行队列的其他任务（任务A或者B）。
"""

import asyncio
import time
from datetime import datetime

async def custom_sleep():
    print('SLEEP', datetime.now())
    await asyncio.sleep(1)

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print('Task{}:Compute factorial({})'.format(name, i))
        await custom_sleep()
        f*=i
    print('Task{}:factorial({}) is {}\n'.format(name, number, f))

start = time.time()
loop = asyncio.get_event_loop()

tasks = [asyncio.ensure_future(factorial('A',3)),
        asyncio.ensure_future(factorial('B',4)),
        ]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print("Total time:{}".format(end-start))