# 2.写程序：保存用户名和密码。
# (1).用户名和密码保存在如下数据结构中
# user_list = [
# {‘username’: ‘zs’, ‘password’: ‘1234’},
# {‘username’: ‘ls’, ‘password’: ‘asdf’}
# ]
# (2).非法字符模板board = [‘zs’, ‘ls’, ‘ww’]。
# (3).可连续输入用户名和密码。
# (4).如果想终止程序，请输入Q或者q。
# (5).录入用户名时，如果是board里面的非法字符串，将非法字符串替换成同等数量的* 例如 zs 替换成**。
# 然后添加到user_list中
# (6).每次添加成功后，打印出刚添加的用户名，密码。
user_list = []

board = ['zs', 'ls', 'ww']
while True:
    di = {}
    s = input('请输入用户名和密码，以空格分割，按Q/q退出：')
    if s.lower() == 'q':
        break
    l = s.split()
    if l[0] == s:
        print('未输入密码！')
        continue
    for i in board:
        if i in l[0]:
            l[0] = l[0].replace(i, '*'*len(i))
    di['username'] = l[0]
    di['password'] = l[1]
    user_list.append(di)
    print('用户名：', l[0], '  密码：', l[1])

print(user_list)
