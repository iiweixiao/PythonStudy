
# 封装
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  #私有属性
    def study(self):
        print('今年 ' + str(self.__age) + '岁')
    def info(self):
        print(self.name, self.__age)

james = Person('James', 30)
james.study()

print(james.name)
print(james._Person__age)
# print(dir(james))

# 继承
class Student(Person):
    def __init__(self, name, age, no_):
        super().__init__(name, age)
        self.no_ = no_

class Teacher(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
# 方法重写
    def info(self):
        print(self.name, self._Person__age, self.address)

stu = Student('James', 30, 'No.12')
tea = Teacher('Tony', 40, 'beijing')
stu.info()
tea.info()

# 多继承
class A(object):
    pass
class B(object):
    pass
class C(A, B):
    pass