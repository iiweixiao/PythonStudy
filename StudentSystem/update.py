# 作者:  Bruce
# 时间： 2022/4/20
import time
import os

filename = 'StudentInfo.txt'
# 修改学生信息
str1 = ''
def update():
    while True:
        # 判断学生信息文件是否存在，在的话就提取文件中内容转成列表stu，并提示选择学生id或姓名，不在就退出
        if os.path.exists(filename):
            print('学生信息汇总'.center(60, '-'))
            with open(filename, 'r', encoding='utf-8') as file:
                stu = file.readlines()  # 把txt文件转成列表
                # print(type(stu))  # 返回list
                for s in stu:
                    print(s.strip())  # 打印列表中每一行，为字符串
                    # print(type(s))  # 返回str
            pick = input('请输入要修改学生的id或姓名，id选1，姓名选2：')
        else:
            print('暂无学生信息，即将返回功能菜单...')
            time.sleep(1)
            break
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
                # print(d)
                # print(d['id'])
                if str(d[index]) == key:  # 查找
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
            return update()

        showinfo()
        time.sleep(1)
        answer = input('是否继续修改学生信息？y/n')
        if answer.lower() == 'y':
            continue
        else:
            break

def showinfo():
    print('学生信息汇总'.center(60, '-'))
    with open(filename, 'r', encoding='utf-8') as file:
        stu = file.readlines()  # 把txt文件转成列表
        # print(type(stu))  # 返回list
        for s in stu:
            print(s.strip())  # 打印列表中每一行，为字符串

update()
