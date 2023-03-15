# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 双向链表.py
@time: 2022/12/8 16:59
@参考: 《数据结构与算法图解》
"""
class Node(object):
    '''双向链表的结点'''
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.value}'

class DoubleLinkedList(object):
    '''双向链表'''
    def __init__(self):
        self._head = None
        self._tail = None

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

    def len(self):
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

    def index(self, value):
        cur_node = self._head
        cur_index = 0
        try:
            while cur_node.value != value:
                cur_node = cur_node.next
                cur_index += 1
        except AttributeError:
            raise ValueError(f'value {value} not in DoubleLinkedList')
        return cur_index

    def append(self, value):
        node_new = Node(value)
        if self._head == None:
            self._head = node_new
            self._tail = node_new
        else:
            node_new.prev = self._tail
            self._tail.next = node_new
            self._tail = node_new

    def pop(self):
        if self._head == None:
            raise IndexError('pop from empty LinkList')
        elif self._tail.prev == None:
            delete_node = self._tail
            self._head = None
            self._tail = None
            return delete_node
        else:
            delete_node = self._tail
            self._tail.prev.next = None
            self._tail = self._tail.prev
            return delete_node

    def insert(self, index, value):
        node_new = Node(value)
        if index < 0:
            raise IndexError('index must be positive integer')
        elif index == 0:
            node_new.next = self._head
            self._head.prev = node_new
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
            node_new.prev = cur_node
            cur_node.next = node_new
            node_new.next.prev = node_new

    def delete_by_index(self, index):
        if index == 0:
            self._head = self._head.next
            return
        else:
            prev_node = self._head.prev
            cur_node = self._head

            cur_index = 0
            while cur_index < index:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_index += 1
            try:
                prev_node.next = cur_node.next
            except AttributeError:
                raise IndexError('index out of range')
            try:
                prev_node.next.prev = prev_node
            except:
                self._tail = prev_node
            return cur_node

    def delete_by_value(self, value, n=-1):
        cur_node = self._head
        deleted_number = 0
        while cur_node != None and deleted_number != n:
            if cur_node.value == value:
                try:
                    cur_node.prev.next = cur_node.next
                except:
                    self._head = cur_node.next
                try:
                    cur_node.next.prev = cur_node.prev
                except:
                    self._tail = cur_node.prev
                deleted_number += 1
            cur_node = cur_node.next





if __name__ == '__main__':
    double_link_list = DoubleLinkedList()

    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    double_link_list._head = node0

    node0.next = node1

    node1.next = node2
    node1.prev = node0

    node2.next = node3
    node2.prev = node1

    node3.prev = node2

    double_link_list._tail = node3

    print(double_link_list.len())
    print(double_link_list)
    double_link_list.append(1)
    print(double_link_list)




    double_link_list.delete_by_value(1)
    print(double_link_list)
    print(double_link_list._tail)
    double_link_list.delete_by_value(2)
    print(double_link_list)
    double_link_list.delete_by_value(3)
    print(double_link_list)
    print(double_link_list._tail)
    double_link_list.append(0)
    print(double_link_list)
    double_link_list.delete_by_value(0)
    print(double_link_list)














