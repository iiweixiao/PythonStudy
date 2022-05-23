# 人类
class Person(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password


# 管理员类，继承Person
class Admin(Person):
    school_list = []

    def __init__(self, name, password):
        super().__init__(name, password)

    def create_school(self, school_name, school_addr):
        school = School(school_name, school_addr)
        Admin.school_list.append(school)
        print(f'{self.name} 创建了 {school.name}')
        return school

    def create_coures(self, course_name, course_prize):
        course = Course(course_name, course_prize)
        print(f'{self.name} 创建了 {course.name}课程')
        return course

    def create_teacher(self, teacher_name, teacher_passwd):
        teacher = Teacher(teacher_name, teacher_passwd)
        print(f'{self.name}  招聘  {teacher.name}为老师')
        return teacher


# 教师类，继承Person
class Teacher(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.courses = list()

    def add_course(self, course):
        self.courses.append(course)
        print(f'{self.name} 增加了 {course.name}')

    def scoring(self, student, course, grade):
        print("开始打分")
        if course in student.courses:
            print(f'{self.name} 老师给 {student.name} 的{course.name}打了 {grade}分')
        else:
            print(f'{self.name}老师发现 学生{student.name} 没有购买{course.name}课程')


# 学生类，继承Person
class Student(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.courses = list()
        self.school = ''

    def get_school_list(self, admin):
        for i in admin.school_list:
            print(f'当前学校有{i.name}')

    def choice_school(self, school):
        self.school = school
        print(f'{self.name} 选择了 {school.name}')

    def choice_course(self, course):
        if course.name in self.school.courses:
            self.courses.append(course)
            course.students.append(self.name)
            print(f'{self.name} 选择了 {course.name} 课程')
        else:
            print(f'{self.school.name} 没有 {course.name} 课程')


# 学校类
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.courses = list()

    def add_course(self, course):
        course_name = course.name
        self.courses.append(course_name)
        print(f'{self.name} 学校 增加了 {course_name}课程')


# 课程类
class Course(object):
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
        self.students = list()

    def add_student(self, student):
        self.students.append(student)
        print(f'{student} 学了 {self.name}课程')


# 管理员
admin = Admin('冉宏元', '123')

# 管理员创建了school
bj_school = admin.create_school('北京oldboy教育公司', '北京')
sz_school = admin.create_school('深圳oldboy教育公司', '深圳')
sh_school = admin.create_school('上海oldboy教育公司', '上海')
wh_school = admin.create_school('武汉oldboy教育公司', '武汉')

# 管理员创建了课程
python = admin.create_coures('Python', 21000)
linux = admin.create_coures('Linux', 18000)
go = admin.create_coures('go', 16000)

# 学校增加课程
'''北京'''
bj_school.add_course(python)
bj_school.add_course(linux)
bj_school.add_course(go)
'''上海'''
sh_school.add_course(go)
sh_school.add_course(python)
'''武汉'''
wh_school.add_course(linux)
'''深圳'''
sz_school.add_course(python)
sz_school.add_course(go)

# 管理员招聘老师
nick = admin.create_teacher('nick', '456')
tank = admin.create_teacher('tank', '789')

# 学生
one = Student('张三', '123')
one.get_school_list(admin)
one.choice_school(sh_school)
one.choice_course(linux)
one.choice_course(python)
one.choice_course(go)

two = Student('李四', '123')
two.get_school_list(admin)
two.choice_school(wh_school)
two.choice_course(linux)
two.choice_course(python)
two.choice_course(go)

# 老师给学生打分
nick.scoring(one, linux, 12)

# 打印one学生的课程记录
print("打印one学生的课程记录")
for i in one.courses:
    print(i.name)

print("打印two学生的课程记录")
for i in two.courses:
    print(i.name)

'''打印python课程学习的人'''
for i in python.students:
    print(i)
'''打印linux课程学习的人'''
for i in linux.students:
    print(i)
'''打印go课程学习的人'''
for i in go.students:
    print(i)
