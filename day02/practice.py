class Stu(object):
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def action(self):
        if self.age >= 18:
            print(f"{self.name}今年{self.age}岁，已经成年了")
        else:
            print(f"{self.name}今年{self.age}岁，还是未成年")

stu1 = Stu('Lilei')
stu2 = Stu('Hanmeimei', 23)
stu2.action()
stu1.action()

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('Poly', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()