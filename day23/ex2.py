# 线程之间执行是无序的
import threading
import time


def work1():
    time.sleep(1)
    print("当前的线程:", threading.current_thread().name)


if __name__ == '__main__':
    for _ in range(5):
        sub_thread = threading.Thread(target=work1)
        sub_thread.start()