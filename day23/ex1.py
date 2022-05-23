import threading
import time

# # 带有参数的任务
# def task(count):
#     for i in range(count):
#         print("正在工作....")
#         time.sleep(0.2)
#     else:
#         print("工作结束")
#
#
# if __name__ == '__main__':
#     # 创建子线程
#     task_thread = threading.Thread(target=task, args=(5,))
#     task_thread.start()

# 带有参数的任务
def task(count):
    for i in range(count):
        print("正在工作....")
        time.sleep(0.2)
    else:
        print("工作结束")


if __name__ == '__main__':
    # 创建子线程
    task_thread = threading.Thread(target=task, kwargs={"count": 6})
    task_thread.start()