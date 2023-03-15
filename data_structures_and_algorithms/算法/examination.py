# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: examination.py
@time: 2023/2/27 14:42
"""
import random

class Test():

    test_function = None
    comparator_function = None
    test_obj = None
    comparator_obj = None
    succeed = True

    def isEqual(self):
        # print('self.test_obj, self.comparator_obj:', self.test_obj, self.comparator_obj)
        assert self.test_obj is not None, (
                "'%s' should include a `test_obj` attribute, "
                % self.__class__.__name__
        )
        assert self.comparator_obj is not None, (
                "'%s' should include a `comparator_obj` attribute, "
                % self.__class__.__name__
        )
        if self.test_obj != self.comparator_obj:
            return False
        else:
            return True


class IntListGenerator(Test):

    testTime = 500000
    maxSize = 1000
    maxValue = 1000

    def generateRandomArray(self):
        # random.random()               等概率返回一个范围在 [0, 1) 之间的浮点数。数学上做不到，但是计算机因为精度问题可以做到。
        # random.random() * N           等概率返回一个范围在 [0, N) 之间的浮点数。
        # int(random.random() * N)      等概率返回一个范围在 [0, N-1] 之间的整数。
        length = int(random.random() * (self.maxSize + 1)) # 长度为是 [0, maxSize] 之间的整数
        arr = [i for i in range(0, length+1)]
        for i in range(0, length + 1):
            arr[i] = int(random.random() * (self.maxValue + 1)) - int(random.random() * (self.maxValue + 1)) # 生成范围在 [-maxValue, maxValue] 之间的随机数

        return arr

    def compare(self, **kwargs):
        for i in range(0, self.testTime):
            arr1 = self.generateRandomArray()
            arr2 = arr1.copy()
            self.comparator_obj = self.comparator_function(arr1)
            self.test_obj = self.test_function(arr2, **kwargs)
            # print(self.comparator_obj)
            # print(self.test_obj)
            if not self.isEqual():
                self.succeed = False
                print("test_function: '%s' failed in examination, please check it" % self.test_function.__name__)
                break
            print(i, 'succeess')

if __name__ == '__main__':

    def bubbleSort(nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 1:
            return nums
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    test = IntListGenerator()
    test.test_function = bubbleSort
    test.comparator_function = sorted

    test.compare()
