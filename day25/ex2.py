class Person():

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        if len(name) > 5:
            return
        self.name = name


class ChinesePeople(Person):
    def __init__(self, name, nation):
        Person.__init__(self, name)
        self.nation = nation

    def get_nation(self):
        return self.nation

    def set_nation(self, nation):
        self.nation = nation

    def set_name(self, name):
        if len(name) > 10:
            return
        self.name = name


p = ChinesePeople("李老师", "汉")
p.set_name("abcdehed1111")
print(p.name)

p.set_name("ab")
print(p.name)