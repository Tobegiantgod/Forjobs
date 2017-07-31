#coding: utf-8
"""
    用subprocess来管理子进程，适用于使用系统命令
"""

import subprocess
import os

#1.向子进程输送数据，然后获取子进程的输出信息。

#定义子进程

def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\x24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc

#启动子进程
procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

#获取输出信息
for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])


"""
   像UNIX管道那样，用平行的子进程来搭建平行的链条，把第一个子进程的输出
与第二个子进程的输入联系起来。
"""

#定义另一个子进程函数

def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE,
    )
    return proc

#启动输入输出相连的两组子进程
input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)


#按顺序等待子进程I/O，获取最后的输出
for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err1 = proc.communicate()
    print(out.strip())


