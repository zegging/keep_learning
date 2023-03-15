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


class LinkList(object):
    '''单链表'''
    def __init__(self):
        self._head = None

    def __getitem__(self, index):
        return self.read(index)

    def __str__(self):
        '''返回value列表'''
        l = []
        cur_node = self._head
        while cur_node != None:
            l.append(cur_node.value)
            cur_node = cur_node.next
        return str(l)

    def items(self):
        cur_node = self._head
        while cur_node != None:
            yield cur_node.value
            cur_node = cur_node.next

    def len(self) -> int:
        cur_node = self._head
        length = 0
        while cur_node != None:
            cur_node = cur_node.next
            length += 1
        return length

    def read(self, index):
        cur_node = self._head
        cur_index = 0
        if index < 0:
            raise IndexError('list index out of range')
        else:
            try:
                while cur_index < index:
                    cur_node = cur_node.next
                    cur_index += 1
                if cur_node == None:
                    raise IndexError('list index out of range')
                else:
                    return cur_node
            except AttributeError:
                raise IndexError('list index out of range')

    def index(self, value) -> int:
        cur_node = self._head
        cur_index = 0
        try:
            while cur_node.value != value:
                cur_node = cur_node.next
                cur_index += 1
            return cur_index
        except AttributeError:
            raise ValueError(f'value {value} not in LinkList')

    def append(self, value):
        node_new = Node(value)
        cur_node = self._head
        if self._head == None:
            self._head = node_new
        else:
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = node_new

    def pop(self):
        if self._head == None:
            raise IndexError('pop from empty LinkList')
        if self._head.next == None:
            delete_node = self._head
            self._head = None
            return delete_node
        else:
            prev_node = self._head
            cur_node = self._head.next
            while cur_node.next != None:
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = None
            return cur_node

    def insert(self, index, value):
        node_new = Node(value)
        if index < 0:
            raise IndexError('index must be positive integer')
        elif index == 0:
            node_new.next = self._head
            self._head = node_new
        else:
            cur_node = self._head
            cur_index = 0
            try:
                while cur_index < index-1:
                    cur_node = cur_node.next
                    cur_index += 1
            except AttributeError:
                raise IndexError('list index out of range')
            node_new.next = cur_node.next
            cur_node.next = node_new

    def delete_by_index(self, index):
        if index == 0:
            self._head = self._head.next
            return
        else:
            prev_node = self._head
            cur_node = self._head.next
            cur_index = 1
            while cur_index < index:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_index += 1
            try:
                prev_node.next = cur_node.next
            except AttributeError:
                raise IndexError('index out of range')

    def delete_by_value(self, value, n=-1):
        '''
            将链表中所有值为value的结点删除
        '''
        deleted_number = 0
        try:
            while self._head.value == value and deleted_number != n:
                self._head = self._head.next
                deleted_number += 1
        except AttributeError:
            return
        prev_node = self._head
        try:
            cur_node = self._head.next
        except:
            return
        while cur_node != None and deleted_number != n:
            if cur_node.value == value:
                prev_node.next = cur_node.next
                cur_node = cur_node.next
                deleted_number += 1
            else:
                prev_node = cur_node
                cur_node = cur_node.next

if __name__ == '__main__':
    # 创建链表
    link_list = LinkList()

    # 创建结点
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)


    # 将结点添加到链表
    link_list._head = node0
    # 将第一个结点的next指针指向下一结点
    node0.next = node1
    node1.next = node2
    node2.next = node3

    link_list.insert(2, 'new')
    print(link_list)
    print(link_list.read(4))

    l = []
    for each in link_list.items():
        l.append(each)

    print(l)

    l = []
    for each in link_list:
        l.append(each)

    link_list.insert(1, 0)
    link_list.append(1)
    print(link_list)
    link_list.delete_by_value(0)
    print(link_list)
    link_list.delete_by_value(1)
    print(link_list)
    link_list.delete_by_value(2)
    print(link_list)
    link_list.delete_by_value(3)
    print(link_list)
    link_list.append('new')
    link_list.append('new')
    print(link_list)
    link_list.delete_by_value('new', 3)
    print(link_list)


