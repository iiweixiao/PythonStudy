# 作者:  Bruce
# 时间： 2022/4/19

class Animal(object):
    def eat(self):
        print('动物要吃东西！')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person(Animal):
    def eat(self):
        print('人吃肉')
def func(Animal):
    Animal.eat()

func(Dog())
func(Cat())
func(Person())


class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
c1 = C('haha', 18)
print(c1.__dict__)  # 列出对象c1的属性
print(C.__dict__)  # 列出类C的属性和方法
print(c1.__class__)  # 对象c1由哪个类创建，列出类C
print(C.__bases__)  # 列出类C所有的父类（A和B）
print(C.__base__)  # 列出类C最近的父类（A）
# __add__()方法 等同于'+'
a = 1
b = 2
c = a+b
cc = a.__add__(b)
print(c)
print(cc)
# 重写__add__()方法
class Teacher:
    def __init__(self, name):
        self.name =name
    def __add__(self, other):
        return self.name + ' ' + other.name
    def __len__(self):
        return len(self.name)
t1 = Teacher('James')
t2 = Teacher('Tony')
s = t1 + t2
print(s)
# __len__()方法
l1 = [1, 2, 3, 4, 5]
print(len(l1))
print(l1.__len__())
print(len(t1))

# __new__()方法
print('-----分割线-----')
class Student(object):
    def __new__(cls, *args, **kwargs):
        print(f'__new__方法被调用，cls的id值为{id(cls)}')  # 类对象Student
        obj = super().__new__(cls)  # 创建一个真实的对象 obj = Student()
        print(f'obj 对象被创建出来后，id值为{id(obj)}')
        return obj
    def __init__(self, name, age):
        print(f'__init__方法被调用，self对象的id值为{id(self)}')
        self.name = name
        self.age = age

bb = Student('James', 18) #obj self bb都是同一个对象
print(f'bb对象的id值为{id(bb)}')
cc = Student('James', 18)
print(f'cc对象的id值为{id(cc)}')

print('--------浅拷贝 深拷贝---------')
# 浅拷贝 深拷贝
class Father:
    pass
class Mother:
    pass
class Family:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
fa1 = Father()
fa2 = fa1
print(fa1, fa2)
mo1 = Mother
family = Family(fa1, fa2)
import copy
family2 = copy.copy(family)
print(family, family.father, family.mother)
print(family2, family2.father, family2.mother)
print(family is family2)

list1 = [[1, 2], (30, 40)]
list2 = list(list1)
list1.append(100)
list2.append(100)
print("list1:",list1)
print("list2:",list2)
list1[0].append(3)
list2[0].append(3)
print("list1:",list1)
print("list2:",list2)
list1[1] += (50, 60)
list2[1] += (50, 60)
print("list1:",list1)
print("list2:",list2)
list1.append(200)
# list2.append(200)
print("list1:",list1)
print("list2:",list2)