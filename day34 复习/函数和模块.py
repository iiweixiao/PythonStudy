# 1.输入一个数，使用reduce计算这个数的阶乘

def reduce(n):
    if n == 1:
        return 1
    else:
        return n * reduce(n - 1)


n = int(input('请输入一个数：'))
print(f'{n}的阶乘为：{reduce(n)}')
