''''''
'''利用底层叶结点的大量空闲指针，如果要求严格保持树结构的话就没有办法用，也叫线索二叉树'''
'''
    假设来到当前结点cur，开始时cur来到头结点位置
    1）如果cur没有左孩子，cur向右移动（cur = cur.right）
    2）如果cur有左孩子，找到左子树上的最右结点mostRight（不停迭代.right）：
        a. 如果mostRight的右指针指向空，让其指向cur，然后cur向左移动（cur = cur.left）
        b. 如果mostRight的右指针指cur，让其指向None，然后cur向右移动（cur = cur.right）
    3）cur为None时遍历停止
    
    结点有左树则可以回到两次，结点没有左树可以回到一次
    根据此时cur结点左树的最优结点的右指针是否为cur可以判断是第几次回到自身：
        1. 指向空为第一次
        2. 指向cur为第二次
        
    就是在cur的左子树上转一圈回到cur自己
    
    因为遍历自己左子树的右边界，所以时间代价是O(N)
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def morris(head: TreeNode):
    if head is None:
        return
    cur = head
    mostRight = None
    # 过流程
    while cur is not None:
        # mostRight是cur的左孩子
        mostRight = cur.left
        # 如果没有左孩子直接跳过if内结构，
        if mostRight is not None:
            # mostRight到达左子树的最优结点，停止条件是right不为空也不指向当前结点，这交给下一步去判断
            while mostRight.right is not None and mostRight.right != cur:
                mostRight = mostRight.right

            # 此时的mostRight是左子树的最右结点
            if mostRight.right is None:
                # 第一次来到cur结点
                mostRight.right = cur
                cur = cur.left
                # 回到最外层过流程的while结构体
                continue
            else:
                # 第二次到达cur
                mostRight.right = None
        cur = cur.right


'''morris先序遍历：如果一个结点只能到达它一次，直接打印；可以到达两次，第一次打印'''


def morrisPre(head: TreeNode):
    if head is None:
        return
    cur = head
    mostRight = None
    # 过流程
    while cur is not None:
        # mostRight是cur的左孩子
        mostRight = cur.left
        # 如果没有左孩子直接跳过if内结构，
        if mostRight is not None:
            # mostRight到达左子树的最优结点，停止条件是right不为空也不指向当前结点，这交给下一步去判断
            while mostRight.right is not None and mostRight.right != cur:
                mostRight = mostRight.right

            # 此时的mostRight是左子树的最右结点
            if mostRight.right is None:
                # 第一次来到cur结点
# -----------------------------------------------------------
                print(cur.val)
# -----------------------------------------------------------
                mostRight.right = cur
                cur = cur.left
                # 回到最外层过流程的while结构体
                continue
            else:
                # 第二次到达cur
                mostRight.right = None
# -----------------------------------------------------------
        # 只能到达一次的结点，直接打印
        else:
            print(cur.val)
# -----------------------------------------------------------
        cur = cur.right


'''morris中序遍历：只到达一次的结点直接打印；可以到达两次的结点第二次打印'''

def morrisPre(head: TreeNode):
    if head is None:
        return
    cur = head
    mostRight = None
    # 过流程
    while cur is not None:
        # mostRight是cur的左孩子
        mostRight = cur.left
        # 如果没有左孩子直接跳过if内结构，
        if mostRight is not None:
            # mostRight到达左子树的最优结点，停止条件是right不为空也不指向当前结点，这交给下一步去判断
            while mostRight.right is not None and mostRight.right != cur:
                mostRight = mostRight.right

            # 此时的mostRight是左子树的最右结点
            if mostRight.right is None:
                # 第一次来到cur结点
                mostRight.right = cur
                cur = cur.left
                # 回到最外层过流程的while结构体
                continue
            else:
                # 第二次到达cur
                mostRight.right = None
# -----------------------------------------------------------
        # 两种情况的合并，只能达到一次的时候打印；第一次到达的时候经过了continue直接跳过，第二次到达的时候进入else，然后打印
        print(cur.val)
# -----------------------------------------------------------
        cur = cur.right


'''morris后序遍历：能回到自己两侧的结点，第二次回到的时候逆序打印自己左树的右边界（从下向上）'''