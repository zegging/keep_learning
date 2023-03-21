# 二叉树的递归序，就是不断的返回自己的结点（回到传入参数是这个结点的代码中）
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

def fun(node: TreeNode):
    # <<<第一次到本函数
    if node == None:
        return
    # print(node)
    # 第一次到本函数>>>

    fun(node.left)
    # <<<第二次到本函数

    # 第二次到本函数>>>
    fun(node.right)
    # <<<第三次到本函数

    # 第三次到本函数>>>

l = [TreeNode(i) for i in range(1, 8)]
l.insert(0, TreeNode(0))
l[1].left = l[2]
l[1].right = l[3]
l[2].left = l[4]
l[2].right = l[5]
l[3].left = l[6]
l[3].right = l[7]

head = l[1]



# 在递归序的基础上可以得到三种不同的遍历方式：先序、中序、后序。
# 先序：任意子树都是先头再左最后右：1次打印
# 中序：任意子树都是先左再中最后右：2次打印
# 后序：任意子树都是先左再右最后头：3次打印

# 非递归实现输出
def preOrder(head: TreeNode):
    if head != None:
        stack = []
        stack.append(head)
        while stack:
            head = stack.pop()
            print(head.val, end=' ')
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)

# 判断一棵树是不是搜索二叉树 Binary Search Tree

# 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
# 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
# 任意节点的左、右子树也分别为二叉查找树；
# 没有键值相等的节点

# 我们可以用中序遍历二叉树，如果严格递增，则是搜索二叉树

import sys
min_num = -sys.maxsize - 1
preVal = min_num

# 递归解法
# 中序遍历第二次返回时打印，在这里处理了搜索二叉树判断的逻辑
# def isBST(head: TreeNode):
#     global preVal
#     if head == None:
#         return True
#     isLeftBST = isBST(head.left)
#     if not isLeftBST:
#         return False
#     if head.val <= preVal:
#         return False
#     else:
#         preVal = head.val
#
#     return isBST(head.right)

# 套路法解决搜索二叉树
def isBST(head: TreeNode):
    return process(head).isBST

class ReturnData():
    def __init__(self, max: int, min: int, isBST: bool):
        self.Max = max
        self.Min = min
        self.isBST = isBST

def process(head: TreeNode):
    if head == None:
        return None
    leftData = process(head.left)
    rightData = process(head.right)
    Min, Max = head.val
    if leftData != None:
        Min = min(leftData.Min, Min)
        Max = max(leftData.Max, Max)
    if rightData != None:
        Min = min(rightData.Min, Min)
        Max = max(rightData.Max, Max)
    isBST = True
    if (leftData != None and (not leftData.isBST or leftData.Max >= head.val)) or (rightData != None and (not rightData.isBST or rightData.Min <= head.val)):
        isBST = False
    return ReturnData(Max, Min, isBST)



# 判断一棵树是不是完全二叉树，Complete Binary Tree
# 通过宽度来判断。

# （1）如果一个结点有right但是没有left，返回false。
# （2）在（1）满足的情况下，遇到的第一个left和right不同时存在的结点之后的结点都必须是叶子结点。
# 同时满足（1）（2）的二叉树是完全二叉树

# def isCBT(head: TreeNode):
#     '''
#
#     :param head:
#     :return:
#     '''
#     if head == None:
#         return True
#     leaf = False # 是否遇到过左右不双全的结点，最开始设置为False
#     left = None
#     right = None
#     queue = []
#     queue.insert(0, head)
#     while queue != []:
#         head = queue.pop()
#         left = head.left
#         right = head.right
#         if (leaf and (left != None or right != None)) or (left == None and right != None): # 条件（2）和条件（1）必须同时满足
#             return False
#         if left != None:
#             queue.insert(0, left)
#         if right != None:
#             queue.insert(0, right)
#         if left == None or right == None:
#             leaf = True
#     return True

# 判断一棵树树否是平衡二叉树Balanced Binary Tree（二叉树题目的套路）
# 任意结点的左子树和右子树的高度之差(平衡因子)的绝对值不超过1且它的左子树和右子树都是一颗平衡二叉树。

def isBBT(head: TreeNode):
    return process(head).isBalanced

class ReturnType():
    def __init__(self, isBalanced: bool, height: int):
        self.isBalanced = isBalanced
        self.height = height

def process(head: TreeNode):
    '''

    :param head:
    :return:
    '''
    if head == None:
        return ReturnType(True, 0)
    leftData = process(head.left)
    rightData = process(head.right)

    height = max(leftData.height, rightData.height) + 1
    isBalanced = leftData.isBalanced and rightData.isBalanced and abs(leftData.height-rightData.height) < 2
    return ReturnType(isBalanced, height)

print(isBBT(head))


# 树形DP的套路：左右两子树的信息利用递归交给本树去处理递归解决的问题都可以使用这种套路。即，必须满足最优子结构

# 判断一棵二叉树是不是满二叉树：
# 结点个数n，深度h，满足 n = 2 ^ h -1

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


# leetcode 236. 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

def process(head: TreeNode, fatherMap: dict):
    if head == None:
        return
    fatherMap[head.left] = head
    fatherMap[head.right] = head
    process(head.left, fatherMap)
    process(head.right, fatherMap)

def lowestCommonAncestor(head: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    fatherMap = {head: head}
    process(head, fatherMap)
    set1 = {}
    cur = p
    while fatherMap[cur] != cur:
        set1.add(fatherMap[cur])
        cur = fatherMap[cur]
    set1.add(head)
    cur = q
    while fatherMap[cur] not in set1:
        cur = fatherMap[cur]

    return fatherMap[cur]

# 1. p,q中的一个是另一个的最近公共祖先
# 2. p,q的最近公共祖先是第三个结点

# 后继结点和前驱结点，中序遍历中一个结点的后一个结点和前一个结点

# 二叉树的序列话和反序列化
# 297. 二叉树的序列化与反序列化
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
#


