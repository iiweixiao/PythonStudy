# 21.请分别使用while和for循环打印1000-0的正整数.
n = 1000
while n >= 0:
    print(n, end=' ')
    n -= 1
print('\n---------')
for i in range(1001):
    print(1000-i, end=' ')