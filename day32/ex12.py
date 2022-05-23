# 类装饰器
class ClassDecorator(object):
    def __init__(self, func):
        self.__func =func
    def __call__(self, *args, **kwargs):
        print('调用了类装饰器')
        self.__func()

# 普通装饰器
def decorator(func):
    def inner():
        print('调用了普通装饰器')
        func()
    return inner

@decorator
@ClassDecorator
def show():
    print('我只是一个普通函数！')

show()
