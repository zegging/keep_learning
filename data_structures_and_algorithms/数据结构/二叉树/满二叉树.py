# 判断一棵二叉树是不是满二叉树：
# 结点个数n，深度h，满足 n = 2 ^ h -1
# 结点个数n，深度h，满足 n = 1 << height - 1
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ReturnData():
    def __init__(self, height, nodes):
        self.height = height
        self.nodes = nodes

def process(head: TreeNode):
    if head == None:
        return ReturnData(0, 0)
    leftData = process(head.left)
    rightData = process(head.right)
    height = max(leftData.height, rightData.height)
    nodes = leftData.nodes + rightData.nodes + 1
    return ReturnData(height, nodes)

# main function
def isFBT(head: TreeNode):
    if head == None:
        return True
    data = process(head)
    return data.nodes == (1 << data.height -1)