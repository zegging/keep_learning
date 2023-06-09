from objprint import op

class Person:
    def __init__(self, name):
        self.name = name

class Male(Person):
    def __init__(self, name):
        super().__init__(name)
        # 等价于super(Male, self).__init__(name)
        # 实际上这时Python语言的一个魔法糖，super()会自动寻找自己所在的类作为第一个参数，然后把self作为第二个参数。
        self.gender = 'male'

m = Male('Peter')
op(m)

# <Male 0x2643bcdfca0
#   .gender = 'male',
#   .name = 'Peter'
# >

'''
super(Male, self)首先从self这个object中拿到它的mro，Male-Person-Object

    对于Python中的多继承情况，运行时在搜索对象的属性或方法时，需要遵循一定的顺序规则，这个规则称为：Method Resolution Order (MRO)

然后找到Male在mro中所处的位置，向后挨个class找是否有__init__函数，将找到的第一个bind到self上。

第二个参数决定了使用这个函数的对象和mro，第一个参数决定了在mro这个链上开始的位置。

第二个参数也可以是class而非object，这在classmethod中常用。
'''

class Animal:
    def __init__(self, age):
        self.age = age

class Person(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

class Male(Person):
    def __init__(self, name):
        super(Person, self).__init__(name)
        self.gender = 'male'

m = Male('Peter')
op(m)

# Traceback (most recent call last):
#   File "D:\pythonProject\设计模式\8. super().py", line 42, in <module>
#     m = Male('Peter')
#   File "D:\pythonProject\设计模式\8. super().py", line 39, in __init__
#     super(Person, self).__init__(name)
# TypeError: object.__init__() takes exactly one argument (the instance to initialize)

'''
这时self的mro链为 Male-Person-Animal-Object 此时Person的前一个class为Animal，Animal类的init函数只接收一个参数，所以报错。
'''