# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 6. 快速排序.py
@time: 2023/3/7 15:56
"""
import random
# from ..examination import IntListGenerator

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
    :return: 返回等于部分的左右边界，由于num在list中是存在的，所以一定存在等于部分。等于部分的左右边界就是小于部分的右边界+1、大于部分的左边界-1
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
    # 这里返回的是等于区的左右边界
    return j+1, k-1

def quickSort(arr:list[int], l:int, r:int) -> list[int]:
    # 这里主要是保证传入的参数有意义
    # 假设我们最初传入的数组是[0,1,2,3]，并且swap选择交换的数是r，那么res = (3,3)
    # 那么入口函数中的第二个quickSort传入的参数是(4,3)，这显然是需要返回的递归边界条件
    if l >= r:
        return arr
    swap(arr, l, r)
    res = sort_triple(arr, l, r)
    left_r = res[0]-1
    right_l = res[1]+1
    quickSort(arr, l, left_r)
    quickSort(arr, right_l, r)

# arr = IntListGenerator().generateRandomArray()
arr = [0,1,2,3]
quickSort(arr, 0, len(arr)-1)
print(arr)
if quickSort(arr, 0, len(arr)-1) == arr.sort():
    print('success')

