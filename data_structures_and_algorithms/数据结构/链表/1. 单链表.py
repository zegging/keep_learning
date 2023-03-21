# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 1. 单链表.py
@time: 2023/3/15 20:50
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# leetcode 234. 回文链表
# https://leetcode.cn/problems/palindrome-linked-list/

# 解法一：数组解法，空间复杂度O(n)
# def isPalindrome(head: ListNode) -> bool:
#     '''
#     数组解法，额外空间O(n)
#     :param head: 头结点
#     :return:
#     '''
#     vals = []
#     current_node = head
#     while current_node != None:
#         vals.append(current_node.val)
#         current_node = current_node.next
#     return vals == vals[::-1]


# 解法二：数组解法，空间复杂度是解法一的一半
# def isPalindrome(head: ListNode) -> bool:
#     '''
#     快慢指针，向数组中压入后一半的node，节省一半的空间。注意快指针先走。
#     :param head:
#     :return:
#     '''
#     cur = head
#     second_half = get_second_half(head)
#     while second_half != []:
#         if second_half.pop() != cur.val:
#             return False
#         else:
#             cur = cur.next
#     return True
#
#
# def get_second_half(head: ListNode) -> list:
#     second_half = []
#     fast = head
#     slow = head
#     # 将fast移动两步同时slow移动一步作为原子化的事务，如果成功则进行下一个while语句
#     # .  None
#     # i   2i
#     # 这是快慢指针的核心语句，要注意根据题目具体分析
#     while fast != None:
#         try:
#             fast = fast.next.next
#             if fast != None:
#                 slow = slow.next
#         except:
#             break
#     slow = slow.next
#     while slow != None:
#         second_half.append(slow.val)
#         slow = slow.next
#     return second_half

# def isPalindrome(head: ListNode) -> bool:

# 空间复杂度O(1)
# https://www.bilibili.com/video/BV13g41157hK/?p=6&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=5285
# def isPalindrome(head: ListNode) -> bool:

def getIntersectionNode(headA: ListNode, headB: ListNode) -> [ListNode]:
    '''
    空间复杂度O(1)的做法
    :param self:
    :param head:
    :return:
    '''
    nodea, nodeb = headA, headB
    a, b = 0, 0
    while nodea != None:
        nodea = nodea.next
        a += 1
    while nodeb != None:
        nodeb = nodeb.next
        b += 1
    if nodea != nodeb:
        return None

    nodea, nodeb = headA, headB
    step = a-b
    if step >= 0:
        while step > 0:
            nodea = nodea.next
            step -= 1
    else:
        while step < 0:
            nodeb = nodeb.next
            step += 1
    while True:
        if nodea == nodeb:
            return nodea
        nodea, nodeb = nodea.next, nodeb.next



