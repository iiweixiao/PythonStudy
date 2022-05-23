class A:
    def __init__(self):
        self.a = 0

class B:
    def __init__(self):
        self.b = 20
    def set_a(self, stu, number):
        stu.a = number

class C:
    def __init__(self):
        self.c = 50
        self.li = []
    def create(self):
        bb = B()
        self.li.append(bb)
        return bb

cc =C()
cc.create()
print(cc.li[0].b)
print(cc.create().b)


# aa = A()
# print(aa.a)
#
# bb = B()
# B.set_a(bb)
#
# # stu = A()
# # print(stu.a)
# #
# #
# # teacher = B()
# # teacher.set_a(stu, 90)
# #
# # print(stu.a)
