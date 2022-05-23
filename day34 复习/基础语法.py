# 1.随机生成两个小于100的整数，打印其中一个数的数据类型和存储地址，
# 求这两个数的和、差、积、商、幂运算
import random

n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
print(f'n1为{n1}')
print(f'n2为{n2}')
print(f'n1的数据类型为{type(n1)}，存储地址为{id(n1)}')
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 ** n2)


# 2.求梯形的面积：输入上底和下底和高，输出面积。面积要求保留两位有效数字，
# 如果输入不是数字，通过异常处理捕捉，并重新输入。
def is_digit(s):
    while True:
        try:
            n = eval(input(f'请输入{s}的值：'))
            return n
        except Exception as e:
            print(e, '输入有误，请重新输入:')


a = is_digit('上底')
b = is_digit('下底')
h = is_digit('高')

s = (a + b) * h / 2
print('提醒的面积为：%.2f' % s)

# 3.strings=["a","as","bat","car","dove","python"] 过滤掉长度小于等于2的字符串，并将剩下的字符串转换成大写字母形式。
strings = ["a", "as", "bat", "car", "dove", "python"]
new_strings = []
for string in strings:
    if len(string) <= 2:
        continue
    else:
        new_strings.append(string.upper())
print(new_strings)

# 4.some_tuples=[(1,2,3),(4,5,6),(7,8,9)] 将这个整数元组构成的列表成为一个简单的整数列表。
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = []
for tuple in some_tuples:
    new_list.extend(list(tuple))
print(new_list)

# 5.写出判断⼀个数是否能同时被2和5整除的条件语句, 并且打印对应的结果。
n = int(input('请输入一个整数：'))
print(f'{n}能同时被2和5整除！') if (n % 2 == 0 and n % 5 == 0) else print(f'{n}不能同时被2和5整除！')
