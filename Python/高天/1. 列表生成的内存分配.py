import sys
import dis

l1 = [0,0,0]
l2 = [0 for _ in range(3)]
l3 = [0] * 3
l4 = [0]
l4.append(0)
l4.append(0)

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
print(sys.getsizeof(l3))
print(sys.getsizeof(l4))

# 88
# 88
# 80
# 这是因为可变长度内存需要系统去调用c函数malloc比较慢
# 所以各种语言在实现的时候就会用一定的优化算法去猜"可能未来还会用到多少内存"，来提前申请这部分内存使用
# 在[0]*3这种实现的时候因为第一次已经分配好了内存空间，之后直接将空间相加，没有"重新分配内存，提前申请到更多内存"的这一步，所以实际占用的内存就比其他两个小
# 空列表最少需要56byte，3个元素，因为32位操作系统每个指针需要8byte，所以一共56+3*8=80byte


print('--------------------------------------------------------')
dis.dis("[0,0,0]")
print('--------------------------------------------------------')

dis.dis("[0 for _ in range(3)]")
print('--------------------------------------------------------')

dis.dis("[0] * 3")
print('--------------------------------------------------------')

dis.dis("l4 = [0]\nl4.append(0)\nl4.append(0)")
print('--------------------------------------------------------')


# --------------------------------------------------------
#   1           0 BUILD_LIST               0
#               2 LOAD_CONST               0 ((0, 0, 0))
#               4 LIST_EXTEND              1
#               6 RETURN_VALUE
# --------------------------------------------------------
#   1           0 LOAD_CONST               0 (<code object <listcomp> at 0x7fbb2676bb50, file "<dis>", line 1>)
#               2 LOAD_CONST               1 ('<listcomp>')
#               4 MAKE_FUNCTION            0
#               6 LOAD_NAME                0 (range)
#               8 LOAD_CONST               2 (3)
#              10 CALL_FUNCTION            1
#              12 GET_ITER
#              14 CALL_FUNCTION            1
#              16 RETURN_VALUE
#
# Disassembly of <code object <listcomp> at 0x7fbb2676bb50, file "<dis>", line 1>:
#   1           0 BUILD_LIST               0
#               2 LOAD_FAST                0 (.0)
#         >>    4 FOR_ITER                 4 (to 14)
#               6 STORE_FAST               1 (_)
#               8 LOAD_CONST               0 (0)
#              10 LIST_APPEND              2
#              12 JUMP_ABSOLUTE            2 (to 4)
#         >>   14 RETURN_VALUE
# --------------------------------------------------------
#   1           0 LOAD_CONST               0 (0)
#               2 BUILD_LIST               1
#               4 LOAD_CONST               1 (3)
#               6 BINARY_MULTIPLY
#               8 RETURN_VALUE
# --------------------------------------------------------
#   1           0 LOAD_CONST               0 (0)
#               2 BUILD_LIST               1
#               4 STORE_NAME               0 (l4)
#
#   2           6 LOAD_NAME                0 (l4)
#               8 LOAD_METHOD              1 (append)
#              10 LOAD_CONST               0 (0)
#              12 CALL_METHOD              1
#              14 POP_TOP
#
#   3          16 LOAD_NAME                0 (l4)
#              18 LOAD_METHOD              1 (append)
#              20 LOAD_CONST               0 (0)
#              22 CALL_METHOD              1
#              24 POP_TOP
#              26 LOAD_CONST               1 (None)
#              28 RETURN_VALUE
# --------------------------------------------------------
#
# Process finished with exit code 0
