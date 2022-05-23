# 13.用代码实现将字符串 v = “k1|v1,k2|v2,k3|v3…” 转换成字典 {‘k1’:’v1’,’k2’:’v2’,’k3’:‘v3’..}.

v = 'k1|v1,k2|v2,k3|v3'
# 方法一：
# l = v.split(',')
# l1 = []
# for i in l:
#     l1.append(i.split('|'))
# di = dict(l1)
# print(di)
# print(type(di))

# 方法二：
# s = v.replace("|", ',')
# l = s.split(',')
# di = {}
# i = 0
# while i < len(l):
#     di[l[i]] = l[i+1]
#     i += 2
# print(di)
# print(type(di))

# 方法三：
s = v.replace(',', '|')
l = s.split('|')
l1 = l[::2]
l2 = l[1::2]
di = {}
for x, y in zip(l1, l2):
    di[x] = y
print(di)