# 作者:  Bruce
# 时间： 2022/5/23
# class A:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18
#         self.sex = 'man'
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#
# print(A('haha').sex)
# # print(A('haha').get_age())
# # A('haha').set_age(13)
# # print(A('haha').get_age())
# a = A('haha')
# print(a.get_age())
# a.set_age(13)
# print(a.get_age())

class A:
    def __init__(self, name):
        self.name = name
        self.age = 18
        self.sex = 'man'
    @property
    def age(self):
        return self.__age
        # return 20
    @age.setter
    def age(self, age):
        self.__age = age


print(A('haha').sex)
a = A('haha')
print(a.age)
a.age = 13
print(a.age)
