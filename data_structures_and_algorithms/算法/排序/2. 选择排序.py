# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 2. 选择排序.py
@time: 2023/2/23 16:51
"""

'''
    选择排序就是通过将无序区中最小的数和无序区的第一个数交换来向右增大有序区
    [(有序区) -> (无序区)]
'''
def selectionSort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n <= 1:
        return nums
    for i in range(0, n):
        min_index = i
        min_value = nums[i]
        for j in range(i, n):
            if nums[j] < min_value:
                min_value = nums[j]
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    selectionSort(arr)
    print("选择排序结果：", arr)
