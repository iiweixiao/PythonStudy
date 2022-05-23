def decorator(func):
    def inner(*args, **kwargs):
        print('正在使用修饰器inner函数')
        return func(*args, **kwargs)

    return inner

@decorator
def add_num(*args, **kwargs):
    res = 0
    for i in args:
        res += i
    for j in kwargs.values():
        res += j
    return res
    # print(res)

res = add_num(1, 7, 4, a=7, c=10)
print(res)

@decorator
def pri():
    print('haha')

pri()