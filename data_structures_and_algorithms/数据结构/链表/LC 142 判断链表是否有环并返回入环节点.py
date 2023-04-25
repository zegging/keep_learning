''''''
'''
快慢指针
if fast is None or fast.next is None 意味着无环

快指针先走慢指针后走，相遇的时候慢指针不动，快指针回到链表开头；然后两个指针以1的步长前进
下次相遇就是入环结点处
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        快慢指针做法，空间复杂度O(1)
        参考：https://zhuanlan.zhihu.com/p/33663488 的证明
        :param self:
        :param head:
        :return:
        '''
        slow = head
        fast = head
        while fast: # 因为fast比slow快, 如果不存在环, 只需判断fast是否为空即可
            slow = slow.next
            if fast.next == None: return None
            fast = fast.next.next
            if slow == fast: break # 不能写到while循环的判断条件中, 因为初始slow=head,会无法进入循环, java可以用do{}while;
        if fast == None: return None # 因为fast比slow快, 如果不存在环, 只需判断fast是否为空即可
        # 设a为head到环入口的距离, b为环入口到相遇位置的距离, c为相遇位置到环入口的距离,
        # 即b+c是环的长度, n为两个指针首次相遇时, 快指针走完的环的圈数, 慢指针显然只能一圈也未走完
        # 根据快指针移动距离为慢指针的两倍, 有如下式子
        # 2(a + b) = a + n(b + c) + b
        # 解出 a = nc + nb - b = (n-1)(b+c) + c
        # 因此让一个新的指针指向head ,每次走一步,走完距离a到达环入口,
        # 另外一个指针也每次走一步, 出发位置为快慢指针的首次相遇位置, 也走距离a,
        # 因为其离环入口的距离为c, 因为a % 环长n = c, 走完距离a必定可以到达环入口 ,
        # 这样两个新的慢指针相遇位置即为环的入口
        slow = head # fast = head也一样
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow