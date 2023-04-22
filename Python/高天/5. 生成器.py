# 先看4. 迭代器
import dis


def gen(num):
    while num > 0:
        yield num
        num -= 1
    return

g = gen(5)
first = next(g)

for i in g:
    print(i)

print(g.__class__)
'''
    生成器本质上是一种特殊的迭代器
    g是生成器函数，gen(5)是生成器对象，这是因为在编译时g的代码块中有yield
    g(5)会返回一个生成器对象，使用next的时候才会运行函数本体
'''
def s():
    def gen(num):
        while num > 0:
            yield num
            num -= 1
        return

    g = gen(5)
    first = next(g)

dis.dis(s)

#  24           0 LOAD_CONST               1 (<code object gen at 0x7fbd45e23890, file "/Users/zhangyanguo/Desktop/Python/高天/5. 生成器.py", line 24>)
#               2 LOAD_CONST               2 ('s.<locals>.gen')
#               4 MAKE_FUNCTION            0
#               6 STORE_FAST               0 (gen)
#
#  30           8 LOAD_FAST                0 (gen)
#              10 LOAD_CONST               3 (5)
#              12 CALL_FUNCTION            1
#              14 STORE_FAST               1 (g)
#
#  31          16 LOAD_GLOBAL              0 (next)
#              18 LOAD_FAST                1 (g)
#              20 CALL_FUNCTION            1
#              22 STORE_FAST               2 (first)
#              24 LOAD_CONST               0 (None)
#              26 RETURN_VALUE
#
# Disassembly of <code object gen at 0x7fbd45e23890, file "/Users/zhangyanguo/Desktop/Python/高天/5. 生成器.py", line 24>:
#               0 GEN_START                0
#
#  25           2 LOAD_FAST                0 (num)
#               4 LOAD_CONST               1 (0)
#               6 COMPARE_OP               4 (>)
#               8 POP_JUMP_IF_FALSE       16 (to 32)
#
#  26     >>   10 LOAD_FAST                0 (num)
#              12 YIELD_VALUE
#              14 POP_TOP
#
#  27          16 LOAD_FAST                0 (num)
#              18 LOAD_CONST               2 (1)
#              20 INPLACE_SUBTRACT
#              22 STORE_FAST               0 (num)
#
#  25          24 LOAD_FAST                0 (num)
#              26 LOAD_CONST               1 (0)
#              28 COMPARE_OP               4 (>)
#              30 POP_JUMP_IF_TRUE         5 (to 10)
#
#  28     >>   32 LOAD_CONST               0 (None)
#              34 RETURN_VALUE

'''
    YIELD_VALUE将栈顶的值取出，然后标记frame未执行完，然后return值并退出
    相当于函数g在运行到yield这一行返回值后并不执行下一行，相当于按下了暂停键
    for i in g(5)就是不断的对g(5)进行call next()，就会不断在while结构中运行
    当num = 0后会直接执行return，由于它在生成器函数里，等价于raise StopIteration
    不管有没有return值，都不会被调用next的时候返回
    
    迭代器是将运行的状态保存在iterator中的，而生成器是将运行状态保存在frame中的
'''

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
        return

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node4 = Node('node4')
node1.next = node2
node2.next = node3
node3.next = node4

iterator = iter(node1)
print(next(iterator).name)
print(next(iterator).name)
print(next(iterator).name)
print(next(iterator).name)

print(node1.name)

l = [1,2,3,4]
for i in l:
    if i == 2:
        l.remove(i)
    print(i)
print(l)

print('-------------------------------------')


