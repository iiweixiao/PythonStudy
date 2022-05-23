# 装饰器
# 给函数增加额外功能的函数，本质是闭包
def func_outer(say):
    print('我先说两句')
    def func_inner():
        print('快来看，sb要说话了！！！')
        print('-------')
        say()
    return func_inner

@func_outer  # 等同于下面的say = func_outer(say)，相当于func_inner
def say():
    print('我要说话了！')

# say = func_outer(say)

say()
