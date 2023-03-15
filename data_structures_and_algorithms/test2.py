# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: test2.py
@time: 2023/3/13 15:20
"""
import sys


# 栈逆序
# 利用递归在不影响传入的stack结构的情况下，不使用其他结构返回栈底的元素
# 重点是在整个递归过程中stack是在不断变化的
# 看手机图片

def f(stack: list):
    res = stack.pop()
    if stack == []:
        return res
    else:
        last = f(stack)
        stack.append(res) # 避免丢失刚刚出栈的元素，压回栈中，整个递归过程中只有栈底元素没有被压回来
        return last

def reverse(stack: list):
    if stack == []:
        return
    i = f(stack)
    reverse(stack)
    stack.append(i)

# leetcode 91.解码方法 https://leetcode.cn/problems/decode-ways/

def process(str:str, i:int):
    if i == len(str):
        return 1
    if str[i] == '0':
        return 0
    if str[i] == '1':
        res = process(str, i+1)
        if i+1 < len(str):
            res += process(str, i+2)
        return res
    if str[i] == '2':
        res = process(str, i+1)
        if i+1 < len(str) and str[i+1] in ['0','1','2','3','4','5','6']:
            res += process(str, i+2)
        return res
    # 数字是3456789的时候只能有一种情况，即解码出它本身对应的数，并不会增加可能性。
    return process(str, i+1)

# n = process('226', 0)
# print(n)


# N皇后问题 leetcode 51.N皇后 https://leetcode.cn/problems/n-queens/

# def isValue(i, j, record):
#     for line in range(0,i): # j需要满足：对0到i-1行的每一行：
#         if j == record[line] or abs(j-record[line]) == abs(line-i): # 不共列，不共斜线
#             return False
#     return True
#
# def processNQueen(i: int, n: int, record:list[int]) -> int:
#     '''
#     :param i: 第i行
#     :param n: 一共几行
#     :param record: 填过的皇后的行列记录
#     :return:
#     '''
#     res = 0
#     if i == n:
#         return 1
#     j = 0
#     while j < n:
#         if isValue(i, j, record):
#             record[i] = j # 将record的第i位上的数字记为棋盘上第i行上放置的皇后的列数（J）
#             res += processNQueen(i+1, n, record)
#         j += 1
#
#     return res
#
# res = processNQueen(0,4, [-1]*4)
# print(res)


# N皇后的位运算加速写法

# python中整型结构中的数组，每个元素最大存储 15 位的二进制数（不同位数操作系统有差异32位系统存15位，64位系统是30位）。如64位系统最大存储30位的二进制数，即存储的最大十进制数是 2^30-1 = 1073741823，也就是说上面例子中数组一个元素存储的最大值是1073741823。

# 由于Python中的int有一个基础内存占用（也就是长整形结构中PyObject_VAR_HEAD占用内存的大小，24字节），因此数字 1 ~ 2^30-1 内存大小是28字节，2^30 ~ 2^60-1 内存大小是32字节，这里需要注意的是 0 占用的内存大小是24字节而非28字节！

# print("2^30 = {}\n2^60 = {}".format(pow(2,30), pow(2,60)))
#
# print("0, 1, 2^30-1, 2^30, 2^60-1, 2^60 的字节大小: ",
#       sys.getsizeof(0), sys.getsizeof(1),
#       sys.getsizeof(1073741823),
#       sys.getsizeof(1073741824),
#       sys.getsizeof(1152921504606846975),
#       sys.getsizeof(1152921504606846976))
#
# # 2^30 = 1073741824
# # 2^60 = 1152921504606846976
# # 0, 1, 2^30-1, 2^30, 2^60-1, 2^60 的字节大小:  24 28 28 32 32 36

# N皇后问题就用三个长度为N的二进制数来作为限制col、l、r

def isValue():
    '''
    0 0 0 0     第0行的列限制：    0 0 0 0
    0 0 0 0     第0行的左斜限：    0 0 0 0
    0 0 0 0     第0行的右斜限：    0 0 0 0
    0 0 0 0     第0行的总限制：    0 0 0 0

    0 1 0 0     第1行的列限制：    0 1 0 0
    0 0 0 0     第1行的左斜限：    1 0 0 0
    0 0 0 0     第1行的右斜限：    0 0 1 0
    0 0 0 0     第1行的总限制：    1 1 1 0

    0 1 0 0     第2行的列限制：    0 1 0 1
    0 0 0 1     第2行的左斜限：    0 0 1 0
    0 0 0 0     第2行的右斜限：    0 0 0 1
    0 0 0 0     第2行的总限制：    0 1 1 1

    0 1 0 0     第3行的列限制：    1 1 0 1
    0 0 0 1     第3行的左斜限：    0 0 1 0
    1 0 0 0     第3行的右斜限：    0 0 0 1
    0 0 0 0     第3行的总限制：    0 1 1 1
    '''
    pass

def processNQueen(N:int, col:int, l:int, r:int):
    '''
    N皇后问题就用三个长度为N的二进制数来作为限制col、l、r
    :param N:
    :param col: 列限制
    :param l: 左斜限制
    :param r: 右斜限制
    :return:
    '''
    limit = (1<<N) - 1 # limit写为二进制：111...11 N个1
    if col == limit: # 意味着每一列都有一个皇后了，存在这样的一个解决方案
        return 1
    pos = limit & (~(col|l|r)) # 和limit做按位与运算是为了l不超出界限：1 0 0 0 -> 1 0 0 0 0
    res = 0
    while pos != 0:
        rightOne = pos & (~pos+1)
        pos = pos - rightOne
        res += processNQueen(N, col|rightOne, (l|rightOne)<<1, (r|rightOne)>>1)
    return res

res = processNQueen(4, 0, 0, 0)
print(res)



