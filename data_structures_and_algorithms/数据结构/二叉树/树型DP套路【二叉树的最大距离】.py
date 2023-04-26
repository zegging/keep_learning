'''二叉树的最大距离：一个结点到另一个结点经过的边的数量，结点只能经过一次'''
'''
    树型DP套路：
    
    【使用前提】
    
    如果题目求解目标是S规则，则求解流程可以定为【以每一个节点为头结点的子树在规则S下的每一个答案，向上传递决策结果】
    
    常见的可能性分类是根据【子树上的头结点是否参与所求结果】
'''

'''
        
    在本题中可以将情况分为
    
    1. 最长路径经过head
        左子树上离head最远的结点经过head后到右子树上最远的结点
        最远结点的距离就是子树的height+1
        所以dis = 左h + 1 + 右h + 1
        

    2. 最长路径不经过head
        那么最大距离可能来自于head的左子树或者右子树，我们需要比较两个子树的两个最大距离的大小（因为不经过head，所以没法联通）
        a. 左子树上的最大距离
        b. 右子树上的最大距离 
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Info():
    def __init__(self, max_distance, height):
        self.max_distance = max_distance
        self.height = height

def process(head: TreeNode):
    if head is None:
        return Info(0, 0)

    leftInfo = process(head.left)
    rightInfo = process(head.right)

    p1 = leftInfo.max_distance
    p2 = rightInfo.max_distance
    p3 = leftInfo.height + rightInfo.height + 2
    max_distance = max(p3, (p1,p2))
    height = max(leftInfo.height, rightInfo.height) + 1
    return Info(max_distance, height)

def main(head):
    return process(head).max_distance
