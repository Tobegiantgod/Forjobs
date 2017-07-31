#coding: utf-8
"""用concurrent.futures的ProcessPoolExecutor调用multiprocess，实现真正的并行"""

""" multiprocess的开销较大，原因在于：主进程与子进程之间，必须进行序列化与反序列化操作。
    程序中的大量开销正是由于这些操作所引发的。所以用ProcessPoolExecutor类来使用多进程
    multiprocess时，更适合于那些只需要小部分数据传输就可以进行大量计算的操作。当这样不
    能提高效率时，再考虑使用multiprocessing模块中的复杂特性。"""

from concurrent.futures import ProcessPoolExecutor
from time import time
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0 ,-1):
        if a % i == 0 and b % i == 0:
            return  i

numbers = [(13456316,4564732), (45664684,45654654), (456456548,2354654)]
start1 = time()
results1 = list(map(gcd, numbers))
end1 = time()
print('single process took %.3f seconds' % (end1-start1))


start2 = time()
pool = ProcessPoolExecutor(max_workers=2)
results2 = list(pool.map(gcd, numbers))
end2 = time()
print('multiprocess took %.3f seconds' % (end2-start2))
