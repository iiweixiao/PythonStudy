# 作者:  Bruce
# 时间： 2022/4/20
import time
import os

filename = 'StudentInfo.txt'
# 删除学生信息
def dele():
    while True:
        # 判断学生信息文件是否存在，在的话就提取文件中内容转成列表stu，并提示输入学生id，不在就退出
        if os.path.exists(filename):
            print('学生信息汇总'.center(60, '-'))
            with open(filename, 'r', encoding='utf-8') as file:
                stu = file.readlines()  # 把txt文件转成列表
                # print(type(stu))  # 返回list
                for s in stu:
                    print(s.strip())  # 打印列表中每一行，为字符串
                    # print(type(s))  # 返回str
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
        showinfo()
        time.sleep(1)
        answer = input('是否继续删除？y/n')
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
            # print(type(s))  # 返回str

dele()
