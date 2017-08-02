#coding: utf-8
"""考虑用协程来并发的运行多个函数"""

"""
线程有以下缺点：
    1.为了确保数据安全，必须使用特殊的工具来协调线程（例如加锁）。使得多线程代码要比单线程代码难懂，
也难以扩展与维护。
    2.线程需要占用大量内存，每个正在执行的线程，大约占据8MB的内存。
    3.线程启动时开销较大。如果不停地依靠创建新线程来同时执行多个函数，线程所引发的开销，就会拖慢整
个程序。
"""

"""
    Python的协程(coroutine)可以避免以上问题，使得Python程序看上去好像是在同时运行多个函数。协程的
实现方式，实际上是对生成器的一种扩展。启动生成器所需的开销与调用函数的开销相仿。处于活跃状态的协程，
在其耗尽之前，只会占用不到1KB的内存。
"""
"""
    每当生成器函数执行到yield表达式的时候，消耗生成器的那段代码，通过send方法给生成器回传一个值。而
生成器经由send函数所传进来的这个值以后，会将其视为yield表达式的执行结果。同时推进到下一个yield表达
式处等待send方法。
"""

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it)
print(it.send(10))
print(it.send(6))
print(it.send(7))
print(it.send(3))

