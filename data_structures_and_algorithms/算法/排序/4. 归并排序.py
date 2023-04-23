# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 4. 归并排序.py
@time: 2023/3/6 17:25
"""

'''
    归并排序是通过不断二分形成最小的比较单元 arr[i] ，
    然后按照顺序从二分得到的两个有序数组中取数比较，合并为一个新的有序数组，
    再将新数组赋值给 arr 
    然后操作下一个分支。
    
    涉及到和之后的元素不重复也不遗漏地比较一次的情况都可以使用并归排序，求小和和求逆序对总数都是这样
'''

def merge(arr:list[int], l:int, mid:int, r:int):
    '''
    :param arr:
    :param l:
    :param mid:
    :param r:
    :return:
    '''
    res = []
    p1 = l
    p2 = mid + 1
    while p1 <= mid and p2 <= r:
        if arr[p1] <= arr[p2]:
            res.append(arr[p1])
            p1 += 1
        else:
            res.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        res.append(arr[p1])
        p1 += 1
    while p2 <= r:
        res.append(arr[p2])
        p2 += 1
    for i in range(0,r-l+1):
        arr[l+i] = res[i]

def mergeSort(arr: list[int], l:int, r:int):
    '''
    :param arr:
    :param l:
    :param r:
    :return:
    '''
    if l == r:
        return arr[l]
    mid = l + ((r-l) >> 1)
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)

arr = [0,2,-1,3]
mergeSort(arr,0,3)
print(arr)

# 利用merge sort求小和

'''
1 3 4 2 5 的小数之和为：
1左侧比1小的数之和为0（规定）
3左侧比3小的数之和为1
4左侧比3小的数之和为4
2左侧比2小的数之和为1
5左侧比5小的数之和为10
所以数组的小数之和为16.

等价于：
1 右侧比 1 大的数有 4 个，则在小数的计算中 有 1 * 4 = 4
3 右侧比 3 大的数有 2 个，则在小数的计算中 有 3 * 2 = 6
4 右侧比 4 大的数有 1 个，则在小数的计算中 有 4 * 1 = 4
2 右侧比 2 大的数有 1 个，则在小数的计算中 有 2 * 1 = 2
5 右侧比 5 大的数有 0 个，则在小数的计算中 有 5 * 0 = 0
小数之和为16

这就相当于在 merge sort 时，一个数都被不重复不遗漏地和其右侧的数比较过一次
在这个比较过程中就可以计算小数之和
'''

# xiaohe = 0
#
# def merge(arr:list[int], l:int, mid:int, r:int):
#     '''
#     :param arr:
#     :param l:
#     :param mid:
#     :param r:
#     :return:
#     '''
#     global xiaohe
#     res = []
#     p1 = l
#     p2 = mid + 1
#     while p1 <= mid and p2 <= r:
#         if arr[p1] <= arr[p2]:
#             xiaohe += arr[p1] * (r - p2 + 1) # 这一步是计算小数之和的重点，参考左程云的视频https://www.bilibili.com/video/BV13g41157hK/?p=4&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=3651
#             res.append(arr[p1])
#             p1 += 1
#         else:
#             res.append(arr[p2])
#             p2 += 1
#     while p1 <= mid:                     # 如果存在p1<=mid，那么意味着上一步进行的是else中的操作，所以arr[r]比arr[p1:mid]中的数都要小（左边的列表已经是有序的了），所以不产生等价的小数
#         res.append(arr[p1])
#         p1 += 1
#     while p2 <= r:
#         res.append(arr[p2])
#         p2 += 1
#     for i in range(0,r-l+1):
#         arr[l+i] = res[i]
#
# def mergeSort(arr: list[int], l:int, r:int):
#     '''
#     :param arr:
#     :param l:
#     :param r:
#     :return:
#     '''
#     if l == r:
#         return arr[l]
#     mid = l + ((r-l) >> 1)
#     mergeSort(arr, l, mid)
#     mergeSort(arr, mid+1, r)
#     merge(arr, l, mid, r)
#
# mergeSort([1,3,4,2,5], 0,4)
# print(xiaohe)

# 利用merge sort求逆序对

# num = 0
#
# def merge(arr:list[int], l:int, mid:int, r:int):
#     '''
#     :param arr:
#     :param l:
#     :param mid:
#     :param r:
#     :return:
#     '''
#     global num
#     res = []
#     p1 = l
#     p2 = mid + 1
#     while p1 <= mid and p2 <= r:
#         if arr[p1] <= arr[p2]:
#             res.append(arr[p1])
#             p1 += 1
#         else:
#             num += mid-p1+1
#             res.append(arr[p2])
#             p2 += 1
#     while p1 <= mid:
#         res.append(arr[p1])
#         p1 += 1
#     while p2 <= r:
#         res.append(arr[p2])
#         p2 += 1
#     for i in range(0,r-l+1):
#         arr[l+i] = res[i]
#
# def mergeSort(arr: list[int], l:int, r:int):
#     '''
#     :param arr:
#     :param l:
#     :param r:
#     :return:
#     '''
#     if l == r:
#         return arr[l]
#     mid = l + ((r-l) >> 1)
#     mergeSort(arr, l, mid)
#     mergeSort(arr, mid+1, r)
#     merge(arr, l, mid, r)
#
# mergeSort([7,5,6,4], 0,3)
# print(num)


# class Solution:
#
#     print('Solution中的变量', locals())
#     def reversePairs(self, nums:list[int]) -> int:
#         print('reversePairs中的变量', locals())
#
#         def mergeSort(l:int, r:int):
#             print('mergeSort中的变量', locals())
#             if l == r:
#                 return nums[l]
#             mid = l + ((r-l) >> 1)
#             mergeSort(l, mid)
#             mergeSort(mid+1, r)
#             merge(l, mid, r)
#             return count
#
#         def merge(l, mid, r):
#
#             print('merge中的变量', locals())
#             # global count
#             # count += 1
#             res = []
#             p1 = l
#             p2 = mid+1
#             while p1 <= mid and p2 <= r:
#                 if nums[p1] <= nums[p2]:
#                     res.append(nums[p1])
#                     p1 +=1
#                 else:
#                     res.append(nums[p2])
#                     p2 += 1
#                     # count += mid - p1 + 1
#             while p1 <= mid:
#                 res.append(nums[p1])
#                 p1 += 1
#             while p2 <= r:
#                 res.append(nums[p2])
#                 p2 += 1
#
#             for i in range(0, r-l+1):
#                 nums[l+i] = res[i]
#
#         l = 0
#         r = len(nums)-1
#         count = 0
#         return mergeSort(l,r)
#
# print('全局变量', locals())
# c = Solution().reversePairs([1,3,2])
#
# print(c)


