# 要求：
# 1.系统运行时，使用一个列表对象来保存注册用户数据。用户查找、修改、删除和添加等操作都针对该列表进行。
# 2.列表中的每个元素为类的实例对象，对象的属性存储注册用户的用户名和登录密码，对象的方法提供修改属性值功能。
# 3.注册用户数据存放在文件中，系统启动时将文件中保存的用户数据列表对象载入到程序中。通过系统菜单选择是否将当前用户数据写入文件保存。
# 4.系统主界面循环显示，每执行完一个菜单操作后，都重新显示主界面，直到选择退出系统。
# 5.设计时，各个菜单操作分别定义一个函数。这样，主界面实现代码的结构非常清晰。
import os.path
import time
import re

# 使用一个列表对象来保存注册用户数据
info = []
# 用于判断增删改后是否保存
# 没保存退出会提示是否保存
is_save = True


class Data(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show(self):
        return f'用户名：{self.name}， 密码：{self.password}'


def menu():
    print('用户数据系统'.center(20, '-'))
    print('1. 添加用户数据')
    print('2. 删除用户数据')
    print('3. 修改用户数据')
    print('4. 查找用户数据')
    print('5. 显示所有数据')
    print('6. 保存当前数据')


def load_data():
    with open('data.txt', 'r', encoding='utf8') as f:
        s = f.readlines()
        for i in s:
            info.append(i.strip())


def add():
    name = input('请输入用户名：')
    password = input('请输入密码：')
    user_data = Data(name, password)
    print(user_data.show(), '\t-->已添加该条信息')
    info.append(user_data.show())
    c = input('按1继续添加，其他任意键返回主菜单：')
    if c == '1':
        add()
    global is_save
    is_save = False


def delete():
    name = input('请输入要删除的用户名：')
    for i in info:
        if name in i:
            print(i)
            s = input('是否删除此对象y/n:')
            if s.lower() == 'y':
                info.remove(i)
            else:
                print('没有删除')
    c = input('按1继续删除，其他任意键返回主菜单：')
    if c == '1':
        delete()
    global is_save
    is_save = False


def change():
    name = input('请输入要修改的用户名：')
    pattern = '用户名：(.*?)，'
    search_info = []
    for i in info:
        if re.findall(pattern, i)[0] == name:
            print(i)
            s = input('是否修改此对象y/n:')
            if s.lower() == 'y':
                info.remove(i)
                name = input('请输入新用户名：')
                password = input('请输入新密码：')
                user_data = Data(name, password)
                info.append(user_data.show())
            else:
                print('此对象没有修改')
                time.sleep(1)
    c = input('按1继续修改，其他任意键返回主菜单：')
    if c == '1':
        change()
    global is_save
    is_save = False


# 查找
def search():
    name = input('请输入要查询的用户名：')
    pattern = '用户名：(.*?)，'
    search_info = []
    flag = False
    for i in info:
        if re.findall(pattern, i)[0] == name:
            search_info.append(i)
            flag = True
    if flag:
        print('查到信息如下：')
        for i in search_info:
            print(i)
    else:
        print('未查到该信息!')
    c = input('按1继续查询，其他任意键返回主菜单：')
    if c == '1':
        search()


# 显示所有数据
def show():
    print('所有用户数据'.center(20, '-'))
    for i in info:
        print(i)
    input('任意键返回主菜单：')


# 通过系统菜单选择是否将当前用户数据写入文件保存。
def save():
    with open('data.txt', 'w', encoding='utf8') as f:
        for i in info:
            f.writelines(i)
            f.writelines('\n')
    global is_save
    is_save = True


def main():
    # 系统启动时将文件中保存的用户数据列表对象载入到程序中
    if os.path.exists('data.txt'):
        load_data()

    flag = True
    while flag:
        # 显示菜单
        menu()
        global is_save
        choice = input('请输入数字选择功能，或按q退出：')
        if choice == '1':
            add()  # 增
        elif choice == '2':
            delete()  # 删
        elif choice == '3':
            change()  # 改
        elif choice == '4':
            search()  # 查
        elif choice == '5':
            show()  # 显示所有数据
        elif choice == '6':
            save()  # 保存到文件
        elif choice.lower() == 'q':
            if not is_save:
                c = input('当前用户数据是否需要写入文件y/n:')
                if c.lower() == 'y':
                    save()
                else:
                    print('数据未保存，即将退出...')
                    time.sleep(1)
            flag = False  # 退出程序
        else:
            print('输入有误，请重新输入！')
            time.sleep(1)


if __name__ == '__main__':
    main()
