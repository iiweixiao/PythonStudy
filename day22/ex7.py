import multiprocessing
import os
import time


# work1
def work1():
    # 获取当前进程编号
    print("work1当前进程编号:", os.getpid())  # work1当前进程编号: 44360
    # 获取当前进程名
    print("work1当前进程名:", multiprocessing.current_process())  # work1当前进程名: <Process name='work1process' parent=44358 started>

    # 获取父进程
    print("work1的父进程：", os.getppid())  # work1的父进程： 44358
    for i in range(5):
        print("1正在工作中....")
        time.sleep(0.2)


# work2
def work2():
    # 获取当前进程编号
    print("work2当前进程编号:", os.getpid())  # work2当前进程编号: 44361
    # 获取当前进程名
    print("work2当前进程名:", multiprocessing.current_process())  # work2当前进程名: <Process name='Process-2' parent=44358 started>
    # 获取父进程
    print("work2的父进程：", os.getppid())  # work2的父进程： 44358
    for i in range(5):
        print("2正在工作中....")
        time.sleep(0.2)


# 主进程
if __name__ == '__main__':
    print("main当前进程编号:", os.getpid())  # main当前进程编号: 44358
    # 创建子进程
    # target是进程执行的目标函数，也就是这个进程分配的对象，name是进程的名字（不写就默认），可写可不写，不过方便后面查看进程的名字我们将第一个子进程起一个名字。
    work1_process = multiprocessing.Process(target=work1, name="work1process")
    work2_process = multiprocessing.Process(target=work2)
    # 启动子进程执行对应的任务
    work1_process.start()
    work2_process.start()
