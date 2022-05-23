# 闭包示例1
def someone(name):
    def say(msg):
        print(f'{name}说：{msg}')
    return say

tom = someone('tom')
jerry = someone('jerry')

tom('hello')
jerry('hello, tom')
tom('come here')
jerry("ok, let's go")

# 闭包修改外部函数变量
def func_outer():
    num1 = 10
    def func_inner():
        nonlocal num1
        num1 = 20
        print(num1)
    return func_inner

f = func_outer()
f()