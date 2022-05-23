s = 'abccba'

flag = True
for i in range(int(len(s) / 2) + 1):
    if s[i] != s[len(s) - 1 - i]:
        flag = False
s1 = '是回文!' if flag else '不是回文!'
print(s, s1)
