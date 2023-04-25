"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
1 -> 1' -> 2 -> 2' -> ...

1 .random -> 3
3. next   -> 3'
1.next    -> 1'
将1'.random指向3'
1'.random -> 1.random.next
'''
class Solution(object):
    def copyRandomList(self, head):
        '''
        不用哈希表和额外结构，空间复杂度为O(1)的解法
        参考：https://www.bilibili.com/video/BV13g41157hK/?p=6&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=6767
        :param head:
        :return:
        '''
        if head == None:
            return None
        cur = head
        while cur != None:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        cur = head
        while cur != None:
            next = cur.next.next # 因为插入过新结点，所以cur.next.next一定存在
            new_node = cur.next
            new_node.random = cur.random.next if cur.random != None else None
            cur = next
            # 还不能破坏现有结构，因为可能会被random指针指向，只有全部遍历完后下一次再进行下一轮
        cur = head
        new_head = cur.next
        while cur != None:
            next = cur.next.next
            new_node = cur.next
            cur.next = next
            new_node.next = next.next if next != None else None
            cur = next
        return new_head