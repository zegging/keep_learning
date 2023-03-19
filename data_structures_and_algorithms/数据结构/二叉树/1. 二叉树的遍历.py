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




