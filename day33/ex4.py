# 作者:  Bruce
# 时间： 2022/5/19
import openpyxl

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😭'
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


# 字符映射
message = input('>')
print(emoji_converter(message))
