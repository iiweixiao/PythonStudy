ss = 'My name is James'
if '2i' or 'w' in ss:
    print('exist')
else:
    print('no')

if ('2i' or 'J') in ss:
    print('exist')
else:
    print('no')

if ('2i' in ss) or ('w' in ss):
    print('exist')
else:
    print('no')

print(4 & 8)
print(4 | 8)
print(4 << 1)  # 乘2
print(4 >> 1)  # 除2

# 运算符优先级
# ()-->算数运算符"**,* / // %, + -, << >>,& |"-->赋值运算符-->布尔运算符-->比较运算符-->位运算符

# 学习调试Debug，按"ctrl+shift+D"，进入debug，按F8执行一个语句，在"Console"界面查看输出
print(' --------程序开始--------- ')
print('1，打开冰箱门')
print('2，把大象放进去')
print('3，关上冰箱门')
print(' --------程序结束---------')

# 32作业
# 学生成绩管理系统,
# 当学生的分数小于60分,打印不及格,请补考
# 当学生的分数大于等于60分,小于80分,打印成绩合格,继续加油
# 当学生的分数大于等于80分,小于等于100分,打印成绩优秀,继续保持
while True:
    score = input("请输入学生成绩：")
    try:
        score = int(score)
    except:
        print("输入类型不正确")
    if type(score) == int:
        if score < 60 and score >= 0:
            print("不及格，请补考")
            break
        elif score < 80:
            print("成绩合格，继续加油")
            break
        elif score <= 100:
            print("成绩优秀，继续保持")
            break
        else:
            print("分数输入不正确")

# 表达式
print("haha" if 1 < 2 else "hehe!")

# 37作业
# 请用代码计算0-1-2-3-4的结果
sum = 0
for i in range(4):
    sum -= i
print('结果是：', sum)

# 列表
x = ['haha', 'nihao', 23]
y = list(['haha', 'nihao', 23])
print(type(x))
print(type(y))
print(id(x))
print(id(y))
print(x == y)
print(x is y)

for i in range(0, 10, 2):
    print(i, end=' ')

xx = ['haha', 'nihao', 23, 'sdfjl']
xx.pop(-2)
print(xx)

di = {'12': 22, '324': 43, 'sdf': 'dxf'}
print(di['324'])
print(di.get('324'))
# print(di['325'])
print(di.get('325'))

print(di.get('325', 8), 7)

qw = ['df', 'haha', 'nihao', 23, 'sdfjl']
ww = ['23ha', 'n43ao', 43, 'sdf43jl']
we = dict(zip(qw, ww))
print(we)
er = {q: w for q, w in zip(qw, ww)}
print(er)

ls = tuple(('dfh', 'efo', 'wwe'))
print(type(ls))

s1 = {1, 2, 3, 4}
s1.add(8)
s1.update({9, 15})
s1.update([11, 12])
s1.update((13, 14))
s1.remove(12) #如果集合中没有12会报错
s1.discard(999) #如果集合中没有999也不会报错
s1.pop()
s1.pop()
print(s1)


s = {1, 2, 3, 4}
s1 = {2, 4, 1, 3}
s2 = {1, 2}
s3 = {1, 5}
print(s == s1) #True
print(s2.issubset(s)) #True 子集
print(s1.issuperset(s1)) #True 超集
print(s1.isdisjoint(s3)) #False 有交集返回False
print(s1.intersection(s2)) #{1, 2} 交集 s1&s2
print(s1.union(s3)) #并集 s1|s3
print(s2.difference(s1)) #差集 s2-s1 小-大=set()
print(s1.symmetric_difference(s2)) #对称差集 s1^s2


