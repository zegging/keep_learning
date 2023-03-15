# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 3. 插入排序.py
@time: 2023/2/23 17:13
"""
'''
    插入排序就是通过将无序区中的第一个数从右到左和有序区中的数比较大小，如果小于就互换位置
    [(有序区) -> (无序区)]
'''


def insertSort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n <= 1:
        return nums
    for i in range(1, n):
        j = i-1
        while j >= 0 and nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1

    return nums

if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    insertSort(arr)
    print("选择排序结果：", arr)
