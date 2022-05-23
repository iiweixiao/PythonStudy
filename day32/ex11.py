# 带参数的装饰器

def return_decorator(flag):
    def decorator(func):
        def inner(*args, **kwargs):
            if flag == '+':
                print('执行加法操作')
            if flag == '-':
                print('执行减法操作')
            return func(*args, **kwargs)
        return inner
    return decorator

@return_decorator('+')
def add_num(*args, **kwargs):
    res = 0
    for i in args:
        res += i
    for i in kwargs.values():
        res += i
    return res

@return_decorator('-')
def sub_num(*args, **kwargs):
    res = 0
    if not args:
        n = 0
        for i in kwargs.values():
            if n == 0:
                res = i
                n += 1
            else:
                res -= i
        return res
    else:
        res = args[0]
        for i in args[1:]:
            res -= i
        for i in kwargs.values():
            res -= i
        return res

print(add_num(1, 3, 5))
print(sub_num(a=1, b=4, c=10))