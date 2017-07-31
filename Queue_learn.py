#conding: utf-8
"""
    使用Queue类来协调管线，它具备阻塞式的队列操作，能够指定缓冲区尺寸，而且还支持join方法，可以防止管线的
的某个阶段陷入持续等待的状态之中，可以在合适的时候停止工作线程，可以防止内存膨胀。
"""

from queue import Queue
from threading import Thread

#定义可关闭的Queue队列，使用task_done()追踪队列的工作进度
class ClosableQueue(Queue):
    CLOSE_SINGAL = object()

    def close(self):
        self.put(self.CLOSE_SINGAL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.CLOSE_SINGAL:
                    return
                yield item
            finally:
                self.task_done()

#定义工作线程
class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        Thread.__init__(self)
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

#工作函数demo
def addone(num):
    num += 1
    return num

def multwo(num):
    num *= 2
    return num

def addtwo(num):
    num += 2
    return num

if __name__ == '__main__':
    first_queue = ClosableQueue()
    second_queue = ClosableQueue()
    third_queue = ClosableQueue()
    fourth_queue = ClosableQueue()

    threads = [ StoppableWorker(addone, first_queue, second_queue),
                StoppableWorker(multwo, second_queue, third_queue),
                StoppableWorker(addtwo, third_queue, fourth_queue),
    ]

    for thread in threads:
        thread.start()

    for i in range(10000):
        first_queue.put(i)
    first_queue.close()
    first_queue.join()
    second_queue.close()
    second_queue.join()
    third_queue.close()
    third_queue.join()
    print(fourth_queue.qsize(), 'items finished')




