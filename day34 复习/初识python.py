# 1、使用while循环输入 1 2 3 4 5 6     8 9 10
n = 1
while n < 11:
    print(n, end=" ")
    n += 1

print('\n-----------分割线-----------')
# 2、求1-100的所有数的和
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

print('\n-----------分割线-----------')
# 3、输出 1-100 内的所有奇数
n = 1
while n < 101:
    print(n, end=' ')
    n += 2
print('\n-----------分割线-----------')

# 4.Hello World的条件输出
# 要求：
# 获得用户输入的一个整数，参考该整数值，打印输出"Hello World"，要求：
# 如果输入值是0，直接输出"Hello World!"
# 如果输入值大于0，输出"Hey you!"
# 如果输入值小于0，输出"Hi Python!"
s = input('请输入一个整数：')
try:
    if int(s) == 0:
        print('Hello World!')
    elif int(s) > 0:
        print('Hey you!')
    elif int(s) < 0:
        print('Hi Python!')
except ValueError:
    print('你输入的不是整数')
# 5.数值运算
# 获得用户输入的一个字符串，M OP N， M和N是任何数字，OP代表一种操作，表示为如下四种：+，-，*，/（加减乘除）
# 根据OP，输出M OP N的运算结果，统一保存小数点后2位。
# 注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。

s1 = input('请输入一个运算：')
print(eval(s1))
# 没能处理一些小数相加导致的精度损失，如0.1 + 0.2 = 0.30000000000000004

