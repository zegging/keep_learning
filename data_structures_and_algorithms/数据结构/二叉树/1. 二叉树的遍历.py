''''''
'''
二叉树的递归序，就是不断的返回小的入口函数中判断是否还有代码需要向下执行
                   1
               2       3
             4   5   6   7
            n n n n n n n n
递归序就是 124442555213666377731
参考：【精准空降到 53:48】 https://www.bilibili.com/video/BV13g41157hK/?p=7&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=3228
'''

# 根据满二叉树的节点编号规则：若根节点编号为 u，则其左子节点编号为 u << 1，其右节点编号为 u << 1 | 1。
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


'''
在递归序的基础上可以得到三种不同的遍历方式：先序、中序、后序。

【先 中 后】指的都是头结点在打印三个结点的时候的相对位置

先序：任意子树都是先头再左最后右【头左右】：1次打印
中序：任意子树都是先左再中最后右【左头右】：2次打印
后序：任意子树都是先左再右最后头【左右头】：3次打印
'''



'''
非递归实现输出
弹出目标栈的时候就打印，所以打印顺序依赖于目标栈的压栈顺序
'''

'''
先序，对与每一颗子树来说打印顺序都是【头左右】

将头结点压入栈

1）从栈中弹出一个结点
2）打印这个弹出结点
3）先右后左将子节点压入栈
4）周而复始

3保证了左结点永远比右结点先弹出并处理

思考？如果压栈的顺序是先左后右呢？-> 后序
'''
def preOrder(head: TreeNode):
    '''
    1. 先弹出结点cur并打印cur
    2. 判断存在，先压入cur右结点再压入cur左结点
    3. 前往1. 步骤

    这样保证每次先弹出头结点并打印，然后因为压栈的顺序，先弹出此head的左节点，然后再弹出此head的右结点。
    :param head:
    :return:
    '''
    if head != None:
        stack = []
        stack.append(head)
        while stack != []:
            head = stack.pop()
            print(head.val, end=' ')
            if head.right != None:
                stack.append(head.right)
            if head.left != None:
                stack.append(head.left)

'''
后序，对与每一颗子树来说打印顺序都是【左右头】

我们需要两个栈帮助处理，一个是中间栈，一个是收集栈，最后打印是从收集栈中弹出打印的。

将头结点压入中间栈

1）从中间栈弹出结点cur
2）并将结点cur压入收集栈
3）将cur子节点【先左后右】压入栈
4）周而复始

直到中间栈为空，将收集栈中的结点依次弹出并打印
'''
def posOrder(head: TreeNode):
    '''
    先初始化两个栈stack1，stack2。1用作中间栈，2用作打印顺序收集栈。1栈中弹出的顺序是‘头右左’，所以2中压入的顺序是‘头右左’，2中弹出打印的顺序是‘左右头’。
    1. 弹出当前结点cur
    2. 把cur压入收集栈
    3. 先压左再压右
    4. 前往1.步骤
    :param head:
    :return:
    '''
    if head != None:
        stack1 = []
        stack2 = []
        stack1.append(head)
        while stack1 != []:
            head = stack1.pop()
            stack2.append(head)
            if head.left != None:
                stack1.append(head.left)
            if head.right != None:
                stack1.append(head.right)
        while stack2 != []:
            print(stack2.pop().val, end=' ')

'''
中序，对与每一颗子树来说打印顺序都是【左右头】

我们初始化一个栈

1）将整棵树的左边界结点全部压入栈中
2）依次弹出结点并打印
3）如果右数不为空，将右树的左边界全部压入栈
4）周而复始，直到栈为空
'''
def inoreder(head: TreeNode):
    '''
    打印顺序是‘左中右’，所以弹出的顺序是‘左中右’，所以head的所有左边界结点都必须先压入栈中。
    整棵树被左边界分解（叶子结点是它自己），对于右树后做操作，保证先打印左树和头结点。
    1. 整棵树的左边界全部先压入栈中
    2. 依次弹出结点的过程中，对右树重复1操作
    :param head:
    :return:
    '''
    if head != None:
        stack = []
        while stack != [] or head != []:
            if head != None:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.val)
                head = head.right


'''
二叉树的优先遍历
二叉树的深度优先遍历就是先序遍历，
二叉树的宽度优先遍历使用队列，就是层序遍历。
参考：https://www.bilibili.com/video/BV13g41157hK/?p=7&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=6355
'''

'''
宽度优先遍历用队列

头 ------> 尾

将头结点压入栈中
1）从尾巴弹出结点
2）将子节点用【先左后右】的顺序压入栈
3）周而复始直到队列为空
'''
def levelOrder(head: TreeNode):
    '''
    :param head:
    :return:
    '''
    if head == None:
        return None
    queueList = []
    queueList.append(head)
    while queueList != []:
        cur = queueList.pop()
        print(cur.val)
        if cur.left != None:
            queueList.insert(0, cur.left)
        if cur.right != None:
            queueList.insert(0, cur.right)                
                


                
                
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

def lowestCommonAncestor(root, p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node):
        if (node == p or node == q or node == None):
            return node
        l = dfs(node.left) 
        r = dfs(node.right)
        if l and r:
            return node
        elif l:
            return l
        elif r:
            return r 
        else:
            return None
    return dfs(root)

# 后继结点和前驱结点，中序遍历中一个结点的后一个结点和前一个结点
# 二叉树的中序后继节点
# 有所不同 剑指 Offer II 053. 二叉搜索树中的中序后继 https://leetcode.cn/problems/P5rCT8/

# 考虑后继节点的情况：
# 1. p有right，则p的后继结点是right的最左结点
# 2. p没有right，如果p是p的父节点的left，则p的后继结点是p的父结点
# 3. p没有right，如果p不是p的父节点的left，则不断上升判断父节点q是不是q的父节点的左结点m，如果是，则返回m
# 4. 最右边的结点没有后继结点，返回None

def getLeftMost(node):
    if node == None:
        return node
    while node.left != None:
        node = node.left
    return node

# 找到二叉树中某个结点的父结点列表
def getFatherNode(head, p):
    if head == p:
        return [head]
    if head == None:
        return
    left = getFatherNode(head.left, p)
    if left:
        left.append(head)
        return left
    right = getFatherNode(head.right, p)
    if right:
        right.append(head)
        return right
    return []

def inorderSuccessor(head: TreeNode, p: TreeNode):
    if p == None:
        return head
    if p.right != None:
        return getLeftMost(p.right)
    else:
        parent_list = getFatherNode(head, p)[::-1]
        if not parent_list:
            return None
        cur = parent_list.pop()
        while parent_list:
            parent = parent_list.pop()
            if cur == parent.left:
                return parent
            cur = parent
        return None

# 二叉树的序列话和反序列化
# 297. 二叉树的序列化与反序列化
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
#


