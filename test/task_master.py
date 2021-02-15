#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random,time,queue
# multiprocessing支持多线程，managers子模块支持把多线程分布到多台机器
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()
def re_task_queue():
    global task_queue
    return task_queue
def re_result_queue():
    global result_queue
    return result_queue
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=re_task_queue)
    QueueManager.register('get_result_queue',callable=re_result_queue)
    # 绑定端口5000，设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    # 启动manager
    manager.start()
    # 获得通过网络访问的Queue对象
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    # 把几个任务放进去
    for i in range(3):
        n = random.randint(0,10000)
        print('Put task %d...' % n)
        task.put(n)
    #从result队列读取结果
    print('Try get results...')
    for i in range(3):
        r = result.get(True) #这样的化就会一直跑。直到结果队列有结果
        # r = result.get(timeout=10)  #而这样等待10s中结果队列如果还没有进来就直接报错了
        print('Result: %s'% r)
    # 关闭
    manager.shutdown()
    print('master exits')