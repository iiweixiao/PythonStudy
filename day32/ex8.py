import time


def decorator(pri):
    def inner():
        begin = time.time()
        pri()
        end = time.time()
        res = end - begin
        print(f'程序一共执行了{res}秒。')
    return inner


@decorator
def pri():
    n = 0
    while n < 5:
        print(n)
        n += 1
    print('执行结束！')
pri()