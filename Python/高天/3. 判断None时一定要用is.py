import dis

a = None

if a:
    print('Not None')

if a == None:
    print('None')

if a is None:
    print('None')

'''
都会得到正确的输出，但是：
1
`if a:` 中会将[],{},set(),False,None都是为bool值为False
'''
class NewList(list):
    def __bool__(self):
        return False
    def __eq__(self, other):
        return True

new_list = NewList([1,2,3])

print(new_list)

if not new_list:
    print('None')

'''
这时会得到输出None，这意味着默认情况下new_list被认为是None
这是因为在NewList中重写了list类的__bool__()函数
'''

if new_list == None:
    print('None')

'''
这时会得到输出None，这意味着默认情况下new_list被认为和None
这是因为在NewList中重写了list类的__eq__()函数
'''

if new_list is None:
    print('None')
else:
    print('Not None')

'''
这时会得到输出Not None，这意味着is正确判断了a
'''

dis.dis('new_list == None')
print('------------------------------------------')
dis.dis('new_list is None')

#   1           0 LOAD_NAME                0 (new_list)
#               2 LOAD_CONST               0 (None)
#               4 COMPARE_OP               2 (==)
#               6 RETURN_VALUE
# ------------------------------------------
#   1           0 LOAD_NAME                0 (new_list)
#               2 LOAD_CONST               0 (None)
#               4 IS_OP                    0
#               6 RETURN_VALUE

'''
原因就是字节码的调用不是一样的，一个是COMPARE_OP，另一个是IS_OP
COMPARE_OP比IS_OP复杂，而且还会调用可能被定义的__eq__或__ne__函数
IS_OP在cpython中的源码是直接比较两个obj的地址，也就是指针比较
所以判断None，直接无脑用is就可以了
'''