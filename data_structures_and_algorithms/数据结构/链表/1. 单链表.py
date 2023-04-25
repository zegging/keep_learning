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
'''
解法一：数组解法，空间复杂度O(n)
等于先将链表从头到尾遍历压栈（额外空间n），然后从栈顶弹出元素，弹出的顺序就是逆序的。
这样的逆序顺序再从链表的头挨个比较，如果到位都对应相等，就说这个链表是逆序的
'''
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

'''
解法二：数组解法，空间复杂度是解法一的一半
利用快慢指针可以得到后半段链表的起始位置（和慢指针相关），注意具体分析

看一下 head.next 是否为None

s = head
f = head
while f is not None ade f.next is not None
    s = s.next
    f = f.next.next

将后半段链表压栈，然后弹出栈顶和链表开头一一比较
'''

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

'''
解法三：空间复杂度O(1)
https://www.bilibili.com/video/BV13g41157hK/?p=6&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=5285

s = head
f = head
while f is not None ade f.next is not None
    s = s.next
    f = f.next.next
    
然后将以s为head的链表反转并返回链表头（右边的1）
        None
          |
1 -> 2 -> 3 <- 2 <- 1
          s
                    f
0    1    2    3    4

从左右两个头一一比较，然后再把链表反转回来                   
'''

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        快慢指针，慢指针指向链表最中间的结点（两个结点都满足取后一个）
        :param head:
        :return:
        '''

        def get_second_half(head: ListNode) -> list:
            fast = head
            slow = head
            # 将fast移动两步同时slow移动一步作为原子化的事务，如果成功则进行下一个while语句
            # .  None
            # i   2i
            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverseList(head: ListNode) -> ListNode:
            cur = head
            prev = None
            while cur != None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev

        cur_1 = head
        second_half_head = get_second_half(head)  # 链表最中间的结点
        head_reverseList = reverseList(second_half_head)  # 反转后半段链表，返回head
        cur_2 = head_reverseList

        while cur_2 != None:
            if cur_1.val == cur_2.val:
                cur_1 = cur_1.next
                cur_2 = cur_2.next
            else:
                return False

        reverseList(head_reverseList)
        return True



