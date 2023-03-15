# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 1. 冒泡排序.py
@time: 2023/2/23 14:13
"""

'''
    冒泡排序就是通过将无序区中最大的数和无序区的最后一个数交换来向左增大有序区
    [(无序区) <- (有序区)]
'''

def bubbleSort(nums: list[int]) -> list[int]:
    n = len(nums)
    if n <= 1:
        return nums
    for i in range(0, n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == '__main__':
    import random


