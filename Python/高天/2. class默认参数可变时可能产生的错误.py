import dis


class Player:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items
        print(id(self.items))

p1 = Player('1')
p2 = Player('2')
p3 = Player('3', ['sword'])

p1.items.append('armor')
p2.items.append('sword')

print(p1.items)
print(p2.items)
print(p3.items)


# 140249450939072
# 140249450939072
# 140249455139584
# ['armor', 'sword']
# ['armor', 'sword']
# ['sword']

dis.dis(Player)

# Disassembly of __init__:
#   6           0 LOAD_FAST                1 (name)
#               2 LOAD_FAST                0 (self)
#               4 STORE_ATTR               0 (name)
#
#   7           6 LOAD_FAST                2 (items)
#               8 LOAD_FAST                0 (self)
#              10 STORE_ATTR               1 (items)
#
#   8          12 LOAD_GLOBAL              2 (print)
#              14 LOAD_GLOBAL              3 (id)
#              16 LOAD_FAST                0 (self)
#              18 LOAD_ATTR                1 (items)
#              20 CALL_FUNCTION            1
#              22 CALL_FUNCTION            1
#              24 POP_TOP
#              26 LOAD_CONST               0 (None)
#              28 RETURN_VALUE


'''
我们可以看到p1，p2玩家的items居然是一样的
这是因为p1，p2初始化的时候用的items是同一个obj
当函数被定义的时候默认值只会被求值一次，之后这个值在每个新的实例被建立的时候都会复用
所以如果默认值是可变对象的话会产生意想不到的bug

官网给出的建议是将默认值设为None，然后在__init__()函数中处理
'''

class Player:
    def __init__(self, name, items=None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items
        print(id(self.items))