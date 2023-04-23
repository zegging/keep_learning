# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 5. 荷兰国旗问题.py
@time: 2023/3/7 13:56
"""
# 题目描述：
# 一个数组arr和一个给定的数num，要求排序后数组的左部分的数均小于等于num，右部分的数均大于num
# 双指针：
# i指向正在判断大小的位置
# j指向小于给定数的范围最右侧位置
# 开始时j指向-1

def sort_double(arr:list[int], num:int) -> list[int]:
    n = len(arr)

    if n == 0:
        return arr
    i = 0

    j = -1
    while i <= n-1:
        if arr[i] <= num:
            arr[i], arr[j+1] = arr[j+1], arr[i] # 将这个小于等于的数转移到小于区的最右边的下一位置，这样整个小于区就相当于向右扩大了一位
            i += 1
            j += 1
        else:
            i += 1
    return arr

arr = sort_double([3,5,6,7,4,3,5,8,-1,20,8,213,-123,0], 5)
print(arr)

# 题目描述：
# 一个数组arr和一个给定的数num，要求排序后数组的左部分的数均小于num，中间部分的数均等于num，右部分的数均大于num
# 三指针：
# i指向正在判断大小的位置
# j指向小于给定数的范围最右侧位置
# k指向大于给定数的范围最左侧位置
# 开始时j指向-1，k指向n=len(arr)
# 当i=k-1时说明数组已经被排序完毕
# 空间复杂度O(1)，时间复杂度O(N)


def sort_triple(arr:list[int], num:int) -> list[int]:
    n = len(arr)

    if n == 0:
        return arr

    i = 0
    j = -1
    k = n
    while i <= k-1:
        if arr[i] < num:
            arr[i], arr[j + 1] = arr[j + 1], arr[i]
            # i位置的数和左部分的下一个数换位
            # [0,...,0(j),1,...1,0(i),...]
            # 等于的部分可能不存在
            i += 1 # 判断下一个数
            j += 1 # 小于部分向右扩大一位
        elif arr[i] == num:
            i += 1
        elif arr[i] > num:
            arr[i], arr[k-1] = arr[k-1], arr[i]
            k -= 1
    return arr

# arr = sort_triple([3,5,6,7,4,3,5,8,-1,20,8,213,-123,0], 5)
arr = sort_triple([6,7,8,9,10], 5)
print(arr)





