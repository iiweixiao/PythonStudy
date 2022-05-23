import time
import os

infos = []  # 用于保存学生信息
filename = 'StudentInfo.txt'


# 功能菜单
def menu():
    while True:
        # os.system('clear')

        print('学生管理系统'.center(40, '-'))
        print('\t\t\t\t1.录入学生信息')
        print('\t\t\t\t2.查找学生信息')
        print('\t\t\t\t3.删除学生信息')
        print('\t\t\t\t4.修改学生信息')
        print('\t\t\t\t5.排序')
        print('\t\t\t\t6.统计学生总人数')
        print('\t\t\t\t7.显示所有学生信息')
        print('\t\t\t\t0.退出程序')
        print(''.center(45, '-'))

        choice = input('请选择（0-7）：')
        if choice.isdecimal() and int(choice) in [0, 1, 2, 3, 4, 5, 6, 7]:
            c = int(choice)
            if c == 0:
                answer = input('确认退出系统y/n:')
                if answer.lower() == 'y':
                    print('感谢使用，再见！')
                    break
                else:
                    continue
            if c == 1:
                insert()
            if c == 2:
                search()
            if c == 3:
                delete()
            if c == 4:
                update()
            if c == 5:
                sort()
            if c == 6:
                total()
            if c == 7:
                show()
                answer = input('返回请按回车键：')

        else:
            print('输入有误！即将返回主菜单！')
            time.sleep(1)

# 1.录入信息
def insert():
    while True:
        is_id = input('请输入学生id，如1001：')
        if is_id.isdecimal() and int(is_id) in range(1000, 2000):
            id = int(is_id)
        else:
            print('无效id！请重新输入！')
            continue
        name = input('请输入学生姓名：')
        if name.strip() == '':
            name = '匿名'
        english = grade('英语')
        math = grade('数学')
        chemistry = grade('化学')
        # 保存学生信息
        student_info = {'id': id, '学生姓名': name, '英语成绩': english, '数学成绩': math, '化学成绩': chemistry}
        infos.append(student_info)

        answer = input('是否再次添加y/n：')
        if answer.lower() == 'y':
            continue
        else:
            break
    save(infos)
    print('学生信息录入完毕！')
    time.sleep(1)

# 2.查找信息
def search():
    while True:
        stu = []
        index = ''
        key = ''
        lst = []
        n = 0
        if os.path.exists(filename):

            print('查找学生信息'.center(45, '-'))

            with open(filename, 'r') as f:
                stu = f.readlines()
                # print(stu)
                for item in stu:
                    d = dict(eval(item))
                    # print(d)
            pick = input('按id查找请输入1，按学生姓名查找请输入2：')
            if str(pick) == '1':
                index = 'id'
                key = input('请输入要查找学生的id：')
            elif str(pick) == '2':
                index = '学生姓名'
                key = input('请输入要查找学生的姓名：')
            else:
                print('输入错误！即将返回...')
                time.sleep(1)
                return search()
            # 循环查找列表stu中的每个字典d有没有对应信息
            flag = True
            for item in stu:
                d = dict(eval(item))
                if str(d[index]) == key:
                    n += 1
                    lst.append(d)
                    flag = False
            if flag:
                print('未找到相关学生信息！')
                time.sleep(1)
                search_pick = input('是否重新查找y/n')
                if search_pick == 'y':
                    return search()
                else:
                    return menu()
            title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
            print(title.format('id', '学生姓名', '英语成绩', '数学成绩', '化学成绩', '总成绩'))
            for i in lst:
                # print(i)

                data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^20}\t{:^2}'
                print(data.format(i.get('id'),
                                  i.get('学生姓名'),
                                  i.get('英语成绩'),
                                  i.get('数学成绩'),
                                  i.get('化学成绩'),
                                  int(i.get('英语成绩'))+int(i.get('数学成绩'))+int(i.get('化学成绩'))
                                  ))
        else:
            print('暂无学生信息！')
            time.sleep(1)
            return menu()

# 3.删除信息
def delete():
    while True:
        # 判断学生信息文件是否存在，在的话就提取文件中内容转成列表stu，并提示输入学生id，不在就退出
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                stu = file.readlines()  # 把txt文件转成列表
                # print(type(stu))  # 返回list
                # for s in stu:
                    # print(s.strip())  # 打印列表中每一行，为字符串
                    # print(type(s))  # 返回str
            show()
            id = input('请输入要删除学生的id：')
        else:
            print('暂无学生信息，即将返回功能菜单...')
            time.sleep(1)
            break
        # 将列表每一行转成字典，循环查找字典中是否有用户输入的id值
        # 循环查字典，找到id值，flag设置为False，提示学生信息已删除
        # 循环查字典，找不到id值，将字典转成字符串合并，最后写入文件中
        with open(filename, 'w', encoding='utf-8') as wfile:
            flag = True
            for s in stu:
                d = dict(eval(s))  # 将str转成dict
                # print(d)
                # print(d['id'])
                if d['id'] == int(id):  # 查找
                    print(f'id为{id}的学生信息已删除！')
                    flag = False
                else:
                    wfile.write(str(d) + '\n')
            if flag:
                print(f'未找到id为{id}的学生信息！')
                time.sleep(1)
        show()
        time.sleep(1)
        answer = input('是否继续删除？y/n')
        if answer.lower() == 'y':
            continue
        else:
            break

# 4. 修改信息
def update():
    index = ''
    key = ''
    while True:
        show()
        with open(filename, 'r', encoding='utf-8') as file:
            stu = file.readlines()  # 把txt文件转成列表
        pick = input('请输入要修改学生的id或姓名，id选1，姓名选2：')

            # 将列表每一行转成字典，循环查找字典中是否有用户输入的id值
        # 循环查字典，找到id值，flag设置为False，提示学生信息已删除
        # 循环查字典，找不到id值，将字典转成字符串合并，最后写入文件中
        if pick == '1':
            index = 'id'
            key = input('请输入学生id：')
        elif pick == '2':
            index = '学生姓名'
            key = input('请输入学生姓名：')
        else:
            print('输入错误!请输入1或2：')
            time.sleep(0.5)
            return update()

        with open(filename, 'w', encoding='utf-8') as wfile:
            flag = True
            for s in stu:
                d = dict(eval(s))  # 将str转成dict
                if str(d[index]) == key:
                    print('即将更新该同学的信息！')
                    d['id'] = input('请更新id：')
                    d['学生姓名'] = input('请更新学生姓名：')
                    d['英语成绩'] = input('请更新英语成绩：')
                    d['数学成绩'] = input('请更新数学成绩：')
                    d['化学成绩'] = input('请更新化学成绩：')
                    wfile.write(str(d) + '\n')
                    time.sleep(0.3)
                    print('信息已更新！')
                    flag = False
                else:
                    wfile.write(str(d) + '\n')
        if flag:
            print('未找到匹配的学生信息')
            time.sleep(1)
        answer = input('继续修改信息吗y/n')
        if answer.lower() == 'y':
            update()
        else:
            menu()

# 5.排序信息
def sort():
    li = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            stu = file.readlines()
            for aa in stu:
                d = dict(eval(aa))
                li.append(d)
        answer = input('英语成绩排名按1，数学成绩排名按2，化学成绩排名按3，总成绩排名按4：')
        if answer == '1':
            sort_input('英语成绩')
        elif answer == '2':
            sort_input('数学成绩')
        elif answer == '3':
            sort_input('化学成绩')
        elif answer == '4':
            sort_input('总成绩')
        else:
            print('输入有误')
            time.sleep(1)
            return sort()
        answer = input('是否重新排序y/n')
        if answer.lower() == 'y':
            return sort()
        else:
            return menu()
    else:
        print('没有学生信息，即将返回功能菜单...')
        time.sleep(1)
        return menu()

# 6.统计人数
def total():
    lst = []

    if os.path.exists(filename):
        print(''.center(45, '-'))

        with open(filename, 'r') as f:
            s = f.readlines()
        print(f'目前系统共有{len(s)}个人！')
    else:
        print('暂无学生信息！即将返回...')
    time.sleep(1)
    input('按回车返回功能菜单！')
    return menu()

# 7.显示信息（不暂停）
def show(a='id',b=False):
    lst = []

    if os.path.exists(filename):
        print('学生信息汇总'.center(45, '-'))

        with open(filename, 'r') as f:
            s = f.readlines()
            for item in s:
                d = dict(eval(item))
                lst.append(d)
                # flag = False
        if a in ['英语成绩', '数学成绩', '化学成绩']:
            lst.sort(key=lambda x: int(x[a]),reverse=b)
        elif a == '总成绩':
            lst.sort(key=lambda x: int(x['英语成绩'])+int(x['数学成绩'])+int(x['化学成绩']), reverse=b)
        title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(title.format('id', '学生姓名', '英语成绩', '数学成绩', '化学成绩', '总成绩'))
        for i in lst:
            data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^20}\t{:^2}'
            print(data.format(i.get('id'),
                              i.get('学生姓名'),
                              i.get('英语成绩'),
                              i.get('数学成绩'),
                              i.get('化学成绩'),
                              int(i.get('英语成绩'))+int(i.get('数学成绩'))+int(i.get('化学成绩'))
                              ))
    else:
        print('暂无学生信息！即将返回...')
        time.sleep(1)

# 将信息存到txt文件中
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

# 返回符合规定的成绩
def grade(str):
    while True:
        a = input(f'请输入{str}成绩：')
        if a.isdecimal() and int(a) in range(101):
            return int(a)
        else:
            print('成绩为0-100的整数！请重新输入！')
            continue

# 排序辅助方法，避免大量重复代码
# 用于选择升序和降序后到学生信息展示
def sort_input(s):
    so = input('升序按1，降序按2：')
    if so == '1':
        show(a=s, b=False)
    elif so == '2':
        show(a=s, b=True)
    else:
        print('输入有误，即将返回...')
        time.sleep(1)
        return sort()

menu()
