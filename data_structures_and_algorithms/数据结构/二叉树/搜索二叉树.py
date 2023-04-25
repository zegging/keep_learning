''''''
'''搜索二叉树：左结点 < 头结点 < 右结点'''

'''
非套路解法
'''
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    preVal = -sys.maxsize - 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        isLeftBST = self.isValidBST(root.left)
        if isLeftBST == False:
            return False
        if root.value <= self.preVal:
            return False
        else:
            self.preVal = root.val

        isRightBST = self.isValidBST(root.right)

        return isRightBST

class Solution:
    preVal = -sys.maxsize - 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []
        self.process(root, l)
        cur = l[0]
        for each in l[1:]:
            if each <= cur:
                return False
            cur = each
        return True


    def process(self, root, l):
        if root is None:
            return
        self.process(root.left, l)
        l.append(root.val)
        self.process(root.right, l)

class Solution:
    preVal = -sys.maxsize - 1
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []
        self.process(root, l)
        cur = l[0]
        for each in l[1:]:
            if each <= cur:
                return False
            cur = each
        return True


    def process(self, root, l):
        if root is None:
            return
        self.process(root.left, l)
        l.append(root.val)
        self.process(root.right, l)
