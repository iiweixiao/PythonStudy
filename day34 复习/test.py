import re

l = [{'用户名': '小黑', '密码': '123'}, {'用户名': '小白', '密码': '456'}]
class A(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def show(self):
        # print(f'用户名：{self.name}， 密码：{self.password}')
        return f'用户名：{self.name}， 密码：{self.password}'

l = []
hei = A('xiaohei', '123')
hei.show()
bai = A('xiaobai', '456')
print(type(hei.show()))
l.append(hei.show())
l.append(bai.show())
bai.name = 'xiaoxiaobai'
l.append(bai.show())
print(l)
info = '用户名：tt，密码：123'
pattern = '用户名：(.*?)，'
# for i in info:
#     if re.findall(pattern, i) == name:
print(re.findall(pattern, info))