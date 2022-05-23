# 1.写程序计算 n 的阶乘 n! 的结果
import random


def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)


print(func(6))

# 2.求1+2!+3!+…+20!的和
print('-------------')


def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n - 1)


sum = 0
for i in range(1, 21):
    sum += func(i)
print(f'1+2!+3!+…+20!的和为:{sum}')

# 3.写程序求表达式 a + aa + aaa + aaaa+ … 的结果，其中a是1~9的数字，求和的项数用n来控制。
print('-------------')
sum = 0
a = random.randint(1, 9)
n = random.randint(1, 9)
print(f'a={a}, n={n}')


def func1(a, n):
    if n == 1:
        return a
    else:
        return 10 * func1(a, n - 1) + a


for i in range(1, n + 1):
    if i < n:
        sum += func1(a, i)
        print(func1(a, i), '+', end=' ')
    else:
        sum += func1(a, i)
        print(func1(a, i), '=', end=' ')
print(sum)

# 4.求整数1~100的累加值，但要求跳过所有个位为3的数。
print('-------------')
sum1 = 0
for i in range(1, 101):
    if i % 10 == 3:
        continue
    else:
        sum1 += i
print(sum1)