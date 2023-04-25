'''平衡二叉树，左右子树的高度差不超过1'''

class ReturnType:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def process(head):
    if head is None:
        return ReturnType(True, 0)

    left = process(head.left)
    right = process(head.right)

    height = max(left.height, right.height)
    isBalanced = left.isBalanced and right.isBalanced and abs(left.height - right.height) < 2

    return ReturnType(isBalanced, height)

def main(head):
    return process(head).isBalanced

'''也可以不平衡返回高度为-2'''
