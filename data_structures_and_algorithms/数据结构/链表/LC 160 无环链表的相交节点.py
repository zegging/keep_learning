# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        空间复杂度O(1)的做法，算走到尾巴时的步数差值
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