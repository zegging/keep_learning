# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 单向循环链表.py
@time: 2022/12/9 13:39
@参考: 《数据结构与算法图解》
"""
class Node(object):
    '''单链表的结点'''
    def __init__(self, value):
        # value存放数据元素
        self.value = value
        # next是下一个节点的标识
        self.next = None
    def __str__(self):
        return f'{self.value}'


class SingleCycleLinkList(object):
    '''单链表'''
    def __init__(self):
        self._head = None


if __name__ == '__main__':
    pass
