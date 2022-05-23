# 1.读取一个python源码文件，显示除了以#号开头的行以外的所有行。并打印输出#号开头的行数。
import os.path
import re

if os.path.exists('面向对象进阶.py'):
    with open('面向对象进阶.py', 'r') as f:
        l = f.readlines()
n = 0
sum = 0
for s in l:
    if re.findall('^#', s.strip()):
        n += 1
    else:
        print(s.strip())
    sum += 1
print(f'以#号开头的行数有{n}行')
print(f'一共{sum}行')

# 2.写一个加法计算器。提示用户输入两个数字，再将它们相加并打印结果。在用户输入的任何一个值不是数字时都捕获异常，并打印一条友好的错误消息。应用异常处理和循环语句，直到用户输入”N“结束程序。
def is_digital(str):
    while True:
        s = input(str)

        if s.lower() == 'n':
            break
        try:
            n = int(s)
            return n
        except ValueError as e:
            print(f'错误原因为{e},\n你输入的不是数字，请重新输入：')

def add(n1, n2):
    print(f'{n1}+{n2}={n1 + n2}')
n1 = is_digital('请输入第一个数字：')
n2 = is_digital('请输入第二个数字：')
add(n1, n2)