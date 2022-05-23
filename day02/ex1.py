# 作者:  Bruce
# 时间： 2022/4/18

s1 = 'aaa'
s2 = 'aaa'
print(s1 is s2)

s3 = 'a%'
s4 = 'a%'
print(s3 is s4)

s = 'james,james'
print(s.index('es'))  # 3
print(s.find('es'))  # 3
print(s.rindex('es'))  # 9
print(s.rfind('es'))  # 9
# print(s.index('h')) # 报错
print(s.find('h'))
# print(s.rindex('h') # 报错
print(s.rfind('h'))

s = 'James, james'
a = s.upper()  # 大写
b = s.lower()  # 小写
c = s.swapcase()  # 切换大小写
d = s.title()  # 第一个字母大写

print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.ljust(20))
print(s.rjust(20, '*'))
print(s.zfill(20))
print(s.zfill(13))
print('123'.zfill(12))

lst = s.split()
lst1 = s.split(sep=',')

print(lst)
print(lst1)

s = "_4re45_"
print(s.isidentifier())  # 判断是否合法，字符串、下划线、数字（不能数字开头）
print(s.isspace())  # 判断指定的字符串是否全部由空白字符组成（回车、换行，水平制表符）
print(s.isalpha())  # 判断指定的字符串是否全部由字母组成
print(s.isdecimal())  # 判断指定字符串是否全部由十进制的数字组成
print(s.isnumeric())  # 判断指定的字符串是否全部由数字组成
print(s.isalnum())  # 判断指定字符串是否全部由字母和数字组成

s = "_4re45_"
print(s.replace('4', '*'))
print(s.replace('4', '*', 1))
l1 = ['1', '2', '3']
l2 = ('1', '2', '3')
print('^'.join(l1))
print(''.join(l2))

print('我是%s，你好' % s)
print('我是{}，你好'.format(s))
print(f'我是{s}，你好')

s = '测试一段中文'
# s = 'This is an apple'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))

s = b'\xb2\xe2\xca\xd4\xd2\xbb\xb6\xce\xd6\xd0\xce\xc4'
print(s.decode(encoding='GBK'))


# 可变参数
def func(*abc):
    print(abc)


func(10, 20, 30)


def func1(**args):
    print(args)


func1(a=10)
func1(a=10, b=20, c=30)


# 递归
# 练习：阶乘
def jc(n):
    if n == 1:
        return 1
    if n > 1:
        return n * jc(n - 1)


n = 4
print(f'{n}的阶乘为：', jc(n))

# bug 异常
try:
    a = int(input("请输入一个数字："))
    b = int(input("请输入一个数字："))
    res = a / b
    print('计算结果为：', res)
except ZeroDivisionError:
    print("除数不可为0")
except ValueError:
    print("只能输入数字")
except BaseException as e:
    print(e)


class Circle(object):
    # 类的属性分为实例属性与类属性两种。
    # 实例属性用于区分不同的实例；
    # 类属性是每个实例的共有属性。
    # 在定义Circle类时，可以为Circle类添加一个特殊的__init__()
    # 方法，当创建实例时，__init__()方法被自动调用为创建的实例增加实例属性。
    pi = 3.14

    # 初始化
    def __init__(self, r):  # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
        self.r = r  # 表示给我们将要创建的实例赋予属性r赋值
    # 实例方法
    def area(self):
        return self.pi * self.r ^ 2
    # 静态方法
    @staticmethod
    def method():  # 可以直接用Circle.method()调用
        pass
    # 类方法
    @classmethod
    def classmethod(cls):  # 可以直接用Circle.classmethod()调用
        pass

c1 = Circle(1)  # 创建实例时直接给定实例属性，self不算在内
c2 = Circle(2)
Circle.pi = 3.1415  # 更改类属性
# 实例名.属性名 访问属性
print(c1.pi)
print(c1.r)
c2.pi = 3.1  # 更改c2实例属性，它将屏蔽掉对类属性的访问
print(c2.pi)
print(c2.r)
# 动态绑定属性
c1.name = '我是圆1'
print(c1.name)
# 动态绑定方法
def roll():
    print('我能滚动')
c1.roll = roll
c1.roll()
