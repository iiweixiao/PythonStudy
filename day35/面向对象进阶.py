# 定义管理员类，管理员有属性(name, password)，可以创建学校、创建课程、创建老师
# 定义老师类，老师有属性(name,password)，可以添加课程、给学生打分,但发现学生没有购买课程时，不能打分，并给出提示
# 定义学生类，学生有属性(name,password)，可以获取当前学校、选择学校、选择课程，但学校没有该课程时，需要提示，并且不能选择该课程
# 定义学校类，学校有属性(name,addr)，可以添加课程
# 定义课程类，课程有属性(name)，可以添加学生

# 管理员类，属性（name，password），方法（创建学校，创建课程，创建老师）
class Administrator:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.schools = []
        self.courses = []
        self.teachers = []

    def add_school(self, name, addr):
        school = Schools(name, addr)
        self.schools.append(name)
        print(f'{self.name}已创建{name}学校，地址在{addr}')
        return school

    def add_course(self, name):
        course = Courses(name)
        self.courses.append(name)
        print(f'{self.name}已创建{name}课程')
        return course

    def add_teacher(self, name, password):
        teacher = Teacher(name, password)
        self.teachers.append(name)
        print(f'{self.name}已创建{name}老师，密码为{password}')
        return teacher

# 老师类，属性(name,password)，方法（添加课程、给学生打分）,但发现学生没有购买课程时，不能打分，并给出提示
class Teacher:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.courses = []

    def join_course(self, name):
        self.courses.append(name)

    def set_score(self, student, course, score):
        if course in student.courses:
            student.scores[course] = score
        else:
            print(f'{student.name}没有选择{course}课程')

# 学生类，属性(name,password)，方法（获取当前学校、选择学校、选择课程），但学校没有该课程时，需要提示，并且不能选择该课程
class Student:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school = ''
        self.courses = []
        self.scores = dict()

    def get_school(self):
        print(f'{self.name}当前的学校为{self.school}')

    def pick_school(self, admin, name):
        if name in admin.schools:
            self.school = name
            print(f'{self.name}选择了{self.school}学校')
        else:
            print('没有该学校！')

    def pick_course(self, school, course):
        if course in school.courses:
            self.courses.append(course)
            print(f'{self.name}已选择{course}课')
        else:
            print(f'{school.name}没有{course}课')

    def show_courses(self):
        print(self.courses)

    def get_score(self, course):
        if course in self.courses:
            print(f'{self.name}的{course}的分数为：{self.scores[course]}')


# 学校类，属性(name,addr)，方法（添加课程）
class Schools:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.courses = []

    def add_course(self, admin, course):
        if course in admin.courses:
            self.courses.append(course)
            print(f'{self.name}已添加{course}课')
        else:
            print(f'{course}这门课没有被{admin.name}创建')

# 课程类，属性(name)，方法（添加学生）
class Courses:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, name):
        self.students.append(name)
        print(f'{self.name}课新增{name}同学')


admin = Administrator('管理员陈', '123456')
bd_school = admin.add_school('北京大学', '北京')
fd_school = admin.add_school('复旦大学', '上海')
yw = admin.add_course('语文')
sx = admin.add_course('数学')
yy = admin.add_course('英语')
bd_school.add_course(admin, '语文')
bd_school.add_course(admin, '化学')  # 化学这门课没有被管理员陈创建
t_w = admin.add_teacher('王老师', '123')
t_s = admin.add_teacher('宋老师', '123')
s_w = Student('王小虎', '123')
s_w.pick_school(admin, '北京大学')
s_w.pick_course(bd_school, '数学')  # 北京大学没有数学课
