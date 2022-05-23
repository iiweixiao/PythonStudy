# 多装饰器
def make_div(func):
    def inner():
        res = '<div>' + func() + '</div>'
        return res
    return inner

def make_p(func):
    def inner():
        res = '<p>' + func() + '</p>'
        return res
    return inner

@make_div
@make_p
def con():
    return '我是一个中国人！'
    # return 66  # 报错

res1 = con()
print(res1)