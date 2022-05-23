# 1.猜数游戏。在程序中预设一个0~9之间的整数，让用户通过键盘输入所猜数字，如果大于预设的数，
# 显示“遗憾，太大了”；如果小于预设的数，显示“遗憾，太小了”；如此循环，直至猜到该数，显示“预
# 测N次，你猜中了！”，其中N是用户输入数字的次数。
import random

n = 1
number = random.randint(0, 9)
print('请输入一个0-9之间的整数：')
print(number)
while True:
    try:
        guess = int(input('>'))
        if guess > number:
            print('遗憾，太大了')
        elif guess < number:
            print('遗憾，太小了')
        elif guess == number:
            break
        n += 1
    except ValueError:
        print('输入不正确')
print(f'猜{n}次，你猜中了！')