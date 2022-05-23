# 作者:  Bruce
# 时间： 2022/5/19
import random

n = random.randint(0, 10)
print('3次以内猜一个0-10之间的数')
print('--------')

total = 0
while  total < 3:
    pick = input('请输入你猜的数字：')
    if pick == str(n):
        print('你猜对了')
        break
    else:
        print('不对，重新猜')

    total += 1

if total == 3:
    print('超过3次了，你输了')

