# 1.有变量name = "alex leNb”完成如下操作:
# 移除name变量对应的值两边的空格，并输出处理结果
name = "alex leNb"
print(name.strip())
# 判断name变量是否以“al”开头，并输出结果(用切片)
print(f'{name}是以"al"开头') if name[0:2] == 'al' else print(f'{name}不是以"al"开头')
# 判断name变量是否以”Nb”结尾,并输出结果(用切片)
print(f'{name}是以"Nb"结尾') if name[-2:] == 'Nb' else print(f'{name}不是以"Nb"结尾')
# 将name 变量对应的值中的所有的”l”替换为“p”,并输出结果
print(name.replace('l', 'p'))
# 将name变量对应的值中的第一个l"替换成”p”,并输出结果
print(name.replace('l', 'p', 1))
# 将name变量对应的值根据所有的”l”分割,并输出结果
print(name.split('l'))
# 将name变量对应的值根据第一个1分割 ,并输出结果
print(name.split('l', maxsplit=1))
# 将name变量对应的值变大写，并输出结果
print(name.upper())
# 将name 变量对应的值变小写,并输出结果
print(name.lower())
# 请输出name变量对应的值的第2个字符?
print(name[1])
# 请输出name变量对应的值的前3个字符?
print(name[0:3])
# 请输出name变量对应的值的后2个字符?
print(name[-2:])


# 2.‘2018-11-12’去掉‘-’输出
s = '2018-11-12'
print(s.replace('-', ''))

# 3.统计字符串a中 1的个数 a=‘201811’
a = '201811'
print(a.count('1'))

# 4.字符串换行输出a = '12345678901234567890’效果如下:
# 1234
# 5678
# 9012
# 3456
# 7890

a = '12345678901234567890'
b = ''
for i in range(0, len(a)):
    if (i + 1) % 4 == 0:
        b += a[i]
        b += '\n'
    else:
        b += a[i]
print(b)