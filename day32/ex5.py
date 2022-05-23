# 作者:  Bruce
# 时间： 2022/5/18
# 闭包
def func_outer():
    num1 = 10

    def func_inner(n):
        num2 = num1 + n
        print(f'num2 = {num2}')

    return func_inner


f = func_outer()
f(5)
f(6)