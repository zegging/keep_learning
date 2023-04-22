import dis

lst = [1,2,3]
for each in lst:
    print(each)

'''
可迭代对象iterable
是一个可以一次返回一个自身元素的对象，for loop in obj中的obj必须是一个iterable
迭代器iterator
表示数据流的对象，可以使用next()函数不断从这个对象中获取数据

iterable更像是一个数据的保存者，一个container，可以完全不知道下一个读取其中的数据的位置信息。
iterable需要有能力产生一个iterator。
从实现上看要么拥有__iter__()，要么有__getitem__()。
这两个函数都是为了保证iterable可以在iter()的作用下返回一个iterator

iterator一定是有状态的，但是它并不一定需要实现一个container
从实现上看必须拥有__next__()，用来返回下一个iterable中的值
'''

dis.dis('lst = [1,2,3]\nfor each in lst:\n\tpass')

#   1           0 BUILD_LIST               0
#               2 LOAD_CONST               0 ((1, 2, 3))
#               4 LIST_EXTEND              1
#               6 STORE_NAME               0 (lst)
#
#   2           8 LOAD_NAME                0 (lst)
#              10 GET_ITER
#         >>   12 FOR_ITER                 2 (to 18)
#              14 STORE_NAME               1 (each)
#
#   3          16 JUMP_ABSOLUTE            6 (to 12)
#
#   2     >>   18 LOAD_CONST               1 (None)
#              20 RETURN_VALUE

'''
GET_ITER这个byte code就是从栈顶的iterable中拿出它所对应的iterator
for loop首先做了一个从iterable中拿到一个iterator的操作，实际的操作对象并不是iterable
'''

class NodeIter:
    def __init__(self, node):
        self.cur_node = node

    def __next__(self):
        if self.cur_node is None:
            raise StopIteration

        node, self.cur_node = self.cur_node, self.cur_node.next
        return node

    def __iter__(self):
        return self

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)

node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node4 = Node('node4')
node1.next = node2
node2.next = node3
node3.next = node4

for node in node1:
    print(node.name)

'''
在这个例子中Node就是一个iterable，NodeIter就是一个iterator
在python的官方文档中要求iterator也必须是一个iterable
所以我们应该实现的NodeIter中需要定义__iter__()函数
'''

print('------------------------------------------------')

iterator = iter(node1)
first = next(iterator)
print(first.name)

for each in iterator:
    print(each.name)

