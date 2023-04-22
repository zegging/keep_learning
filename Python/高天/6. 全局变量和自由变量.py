# b = 6
# def f1(a):
#     print(a)
#     print(b)
#     b = 9
#
# f1(3)
# print(b)

# 3
# Traceback (most recent call last):
#   File "/Users/zhangyanguo/Desktop/Python/高天/5. 生成器.py", line 130, in <module>
#     f1(3)
#   File "/Users/zhangyanguo/Desktop/Python/高天/5. 生成器.py", line 127, in f1
#     print(b)
# UnboundLocalError: local variable 'b' referenced before assignment

'''
    Python不要求声明变量，而是假定在函数定义体中赋值的变量是局部变量。
    如果想让解释器把b当做全局变量，那么需要使用global声明：
'''
import dis

# b = 6
# def f1(a):
#     global b
#     print(a)
#     print(b)
#     b = 9
#
# f1(3)
# print(b)

'''
    初步运行
'''
# count = 0
#
# def f():
#     print(count)
#
# f()
#
# # 0
'''
    error1
'''
# count = 0
#
# def f():
#     count += 1
#
# f()
#
# # Traceback (most recent call last):
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 52, in <module>
# #     f()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 50, in f
# #     count += 1
# # UnboundLocalError: local variable 'count' referenced before assignment
'''
error2
'''
# count = 0
#
# def f():
#     print(count)
#     count += 1
#
# f()
#
# # Traceback (most recent call last):
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 69, in <module>
# #     f()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 66, in f
# #     print(count)
# # UnboundLocalError: local variable 'count' referenced before assignment

s = '''
count = 0
def f():
    print(count)
f()
'''

dis.dis(s)

#   2           0 LOAD_CONST               0 (0)
#               2 STORE_NAME               0 (count)
#
#   4           4 LOAD_CONST               1 (<code object f at 0x7fbce076baa0, file "<dis>", line 4>)
#               6 LOAD_CONST               2 ('f')
#               8 MAKE_FUNCTION            0
#              10 STORE_NAME               1 (f)
#
#   7          12 LOAD_NAME                1 (f)
#              14 CALL_FUNCTION            0
#              16 POP_TOP
#              18 LOAD_CONST               3 (None)
#              20 RETURN_VALUE
#
# Disassembly of <code object f at 0x7fbce076baa0, file "<dis>", line 4>:
#   5           0 LOAD_GLOBAL              0 (print)
#               2 LOAD_GLOBAL              1 (count)
#               4 CALL_FUNCTION            1
#               6 POP_TOP
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE

s1 = '''
count = 0
def f():
    count += 1
f()
'''

dis.dis(s1)

#   2           0 LOAD_CONST               0 (0)
#               2 STORE_NAME               0 (count)
#
#   3           4 LOAD_CONST               1 (<code object f at 0x7f7aae86bc00, file "<dis>", line 3>)
#               6 LOAD_CONST               2 ('f')
#               8 MAKE_FUNCTION            0
#              10 STORE_NAME               1 (f)
#
#   5          12 LOAD_NAME                1 (f)
#              14 CALL_FUNCTION            0
#              16 POP_TOP
#              18 LOAD_CONST               3 (None)
#              20 RETURN_VALUE
#
# Disassembly of <code object f at 0x7f7aae86bc00, file "<dis>", line 3>:
#   4           0 LOAD_FAST                0 (count)
#               2 LOAD_CONST               1 (1)
#               4 INPLACE_ADD
#               6 STORE_FAST               0 (count)
#               8 LOAD_CONST               0 (None)
#              10 RETURN_VALUE

s2 = '''
count = 0
def f():
    global count
    print(count)
    count += 1
f()
'''

dis.dis(s2)

#   2           0 LOAD_CONST               0 (0)
#               2 STORE_GLOBAL             0 (count)
#
#   3           4 LOAD_CONST               1 (<code object f at 0x7fca7e86baa0, file "<dis>", line 3>)
#               6 LOAD_CONST               2 ('f')
#               8 MAKE_FUNCTION            0
#              10 STORE_NAME               1 (f)
#
#   6          12 LOAD_NAME                1 (f)
#              14 CALL_FUNCTION            0
#              16 POP_TOP
#              18 LOAD_CONST               3 (None)
#              20 RETURN_VALUE
#
# Disassembly of <code object f at 0x7fca7e86baa0, file "<dis>", line 3>:
#   5           0 LOAD_GLOBAL              0 (print)
#               2 LOAD_GLOBAL              1 (count)
#               4 CALL_FUNCTION            1
#               6 POP_TOP
#
#   6           8 LOAD_GLOBAL              1 (count)
#              10 LOAD_CONST               1 (1)
#              12 INPLACE_ADD
#              14 STORE_GLOBAL             1 (count)
#              16 LOAD_CONST               0 (None)
#              18 RETURN_VALUE

'''
在s中，当在f中读取count的时候使用的是"2 LOAD_GLOBAL 1 (count)"，读取的是全局变量
在s1中，当在f中读取count的时候使用的是"0 LOAD_FAST 0 (count)"，读取的是局部变量
在s2中，当在f中读取count的时候使用的是"0 LOAD_GLOBAL 0 (count)"，读取的是全局变量

当在函数中对一个变量进行赋值的时候python就会默认这个变量是一个局部变量，无论这个复制在函数中的什么位置
当需要对全局变量进行赋值的时候就需要显式地申明这个变量是全局变量
没有赋值的时候python就会在全局变量里去寻找这个变量
'''

# def g():
#     count = 0
#
#     def f():
#         count += 1
#
#     f()
#     print(count)
#
# g()
#
# # Traceback (most recent call last):
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 198, in <module>
# #     g()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 195, in g
# #     f()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 193, in f
# #     count += 1
# # UnboundLocalError: local variable 'count' referenced before assignment


def g():
    count = 0

    def f():
        count = 1

    f()
    print(count)

g()

# 0
'''
这样的报错是因为在函数f中并没有定义局部变量
输出0是因为f中count = 1赋值的是f中的局部变量而不是g中定义的count
'''

# def g():
#     count = 0
#
#     def f():
#         global count
#         count += 1
#
#     f()
#     print(count)
#
# g()
#
# # Traceback (most recent call last):
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 223, in <module>
# #     g()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 220, in g
# #     f()
# #   File "/Users/zhangyanguo/Desktop/Python/高天/6. 全局变量和自由变量.py", line 218, in f
# #     count += 1
# # NameError: name 'count' is not defined. Did you mean: 'round'?

'''
这样的报错是因为我们在这里需要使用的变量count并不是全局变量count，而是闭包外层的变量
正确的申明方式是使用nonlocal来申明
'''

def g():
    count = 0

    def f():
        nonlocal count
        count = 1

    f()
    print(count)

g()

# 1