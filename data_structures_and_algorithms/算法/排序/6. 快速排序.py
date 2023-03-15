# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 6. 快速排序.py
@time: 2023/3/7 15:56
"""
import random
from 算法.examination import IntListGenerator

'''
    我们需要注意到如果使用 [小于、等于|大于]这种方式做快排，则为0，1排序，即一个元素不是0就是1.因此判断标准是01的都可以做为快排的条件，比如：左面是奇数，右边是偶数。
'''
# 快排参考：【精准空降到 2:02:15】 https://www.bilibili.com/video/BV13g41157hK/?p=4&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=7335
# 时间复杂度O(nlogn)
# 空间复杂度O(logn)


def swap(arr, l, r):
    index = l + int(random.random() * (r-l+1))
    arr[index], arr[r] = arr[r], arr[index] # 交换列表中末尾的数和一个随机位置的数

# 荷兰国旗排序 [小于|等于|大于]
def sort_triple(arr:list[int], l, r):
    '''
    :return: 返回等于部分的左右边界
    '''
    num = arr[r]
    i = l
    j = l-1
    k = r+1
    while i < k:
        if arr[i] < num:
            arr[i], arr[j+1] = arr[j+1], arr[i]
            i += 1
            j += 1
        elif arr[i] == num:
            i += 1
        elif arr[i] > num:
            arr[i], arr[k-1] = arr[k-1], arr[i]
            k -= 1
    return j+1, k-1

def quickSort(arr:list[int], l:int, r:int) -> list[int]:
    if l >= r:
        return arr
    swap(arr, l, r)
    res = sort_triple(arr, l, r)
    left_r = res[0]-1
    right_l = res[1]+1
    quickSort(arr, l, left_r)
    quickSort(arr, right_l, r)

arr = IntListGenerator().generateRandomArray()
if quickSort(arr, 0, len(arr)-1) == arr.sort():
    print('success')

