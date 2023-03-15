# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 7. 堆排序.py
@time: 2023/3/9 13:11
"""
# 以下是大根堆的排序实现

def swap(arr: list[int], index_from: int, index_to: int):
    arr[index_from], arr[index_to] = arr[index_to], arr[index_from]

def heap_insert(arr: list[int], index: int):
    '''
    向上看
    :param arr:
    :param index:
    :return:
    '''
    # while arr[index] > arr[(index-1) >> 1] and index > 0:
    #     swap(arr, index, (index-1) >> 1)
    #     index = (index-1) >> 1

    while arr[index] > arr[int((index-1) / 2)]:
        swap(arr, index, int((index-1) / 2))
        index = int((index-1) / 2)

# arr = [0,1,2,3,4,5,6,7]
# n = len(arr)
# heap_insert(arr, n-1)
# print(arr)

def heap_ify(arr: list[int], index: int, heapSize: int):
    '''
    向下看
    :param arr:
    :param index:
    :param heapSize:堆有效区的大小，末尾索引是heapSize-1
    :return:
    '''
    left = index * 2 + 1
    while left < heapSize:
        # 如果右下孩子存在且值比左下孩子值大，则largest值为右下孩子索引，否则为左孩子索引
        largest = left+1 if left+1 < heapSize and arr[left] < arr[left+1] else left
        # 如果索引largest值比索引index值大，则largest值不变，否则largest值变为index
        largest = largest if arr[largest] > arr[index] else index
        # 如果父结点值不小于子结点值，则循环结束
        if largest == index:
            break
        swap(arr, index, largest)
        # 变换结点索引
        index = largest
        # 计算左孩子结点索引
        left = index * 2 + 1

# arr = [0,1,2,3,4,5,6,7]
# n = len(arr)
# heap_ify(arr, 0 ,8)
# print(arr)

def heapSort(arr: list[int]):
    if arr == None or len(arr) < 2:
        return arr
    heapSize = len(arr)
    # # 相当于将每个数填入数组中使得数组成为大根堆，时间复杂度为O(NlogN)
    # for i in range(heapSize):
    #     heap_insert(arr, i)
    # 相当于从最后开始，将以这个结点为根的小二叉树整理成大根堆
    for i in range(heapSize-1, -1, -1):
        heap_ify(arr, i, heapSize)


    swap(arr, 0, heapSize-1)
    heapSize -= 1
    while heapSize > 0:
        heap_ify(arr, 0, heapSize)
        swap(arr, 0, heapSize-1)
        heapSize -= 1

# arr = [0,1,2,3,4,5,6,7]
# heapSort(arr)
# print(arr)
# for i in range(5,0,-1):
#     print(i)


'''
几乎有序是指如果把数组排好顺序的话，每个元素移动的距离可以不超过k，k为常数且相对于数组大大小来说比较小。
已知一个几乎有序的数组，请选择一个合适的排序算法针对这个数组进行排序

提示：小根堆
'''

# 因为移动距离不超过k，所以数组的最小值一定在arr[0:k]中。
# 则我们可以将arr[0:k]变为小根堆，小根堆的最小值在0位置，同时这个值也是数组的最小值，
# 将小根堆的最小值弹出并赋值给数组0位置，然后将数组k+1位置的数加入小根堆，重新排序
# 重复这个过程
# 时间复杂度O(N)，空间复杂度O(1)

def min_heap_insert(arr: list[int], index: int):
    '''
    向上看
    :param arr:
    :param index:
    :return:
    '''
    while arr[index] < arr[int((index-1) / 2)]:
        swap(arr, index, int((index-1) / 2))
        index = int((index-1) / 2)
    return arr

def min_heap_ify(arr: list[int], index: int, heapSize: int):
    '''
    向下看
    :param arr:
    :param index:
    :param heapSize:
    :return:
    '''
    left = index * 2 + 1
    while left < heapSize:
        smallest = left+1 if left+1 < heapSize and arr[left+1] < arr[left] else left
        smallest = smallest if arr[smallest] < arr[index] else index
        if smallest == index:
            break
        swap(arr, index, smallest)
        index = smallest
        left = index * 2 + 1


def min_heapSort(arr: list[int]):
    if arr == None or len(arr) < 2:
        return arr
    heapSize = len(arr)
    for i in range(heapSize):
        min_heap_insert(arr, i)
    heapSize -= 1
    while heapSize > 0:
        for i in range(heapSize):
            arr[len(arr) - heapSize:] = min_heap_insert(arr[len(arr) - heapSize:], i)
        heapSize -= 1
    return arr

# 以上是小根堆的实现


def k_min_sort(arr: list[int], k: int):
    # 移动k次，即这个小根堆的长度为k+1
    min_heap = arr[0:k+1]
    print(min_heap)
    i = 0
    while i+k+1 < len(arr):
        min_heap = min_heapSort(min_heap)
        print(min_heap)
        arr[i] = min_heap[0]
        print(arr)
        min_heap[0] = arr[i+k+1]
        print(min_heap)
        i += 1
    min_heap = min_heapSort(min_heap)
    print(min_heap)
    j = 0
    while j <= k:
        arr[j-k-1] = min_heap[j]
        j += 1


# arr = [0,2,3,1,-1,7,5,4,6]
# k_min_sort(arr, 4)
# print(arr)