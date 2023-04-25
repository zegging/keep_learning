# 二叉树的递归套路

**当我可以向左树要信息，也可以向我的右树要信息的情况下，可以使用这种递归套路**

我们以平衡二叉树的验证举例。

平衡二叉树中的任意一个结点都必须满足：

* 左子树是平衡的
* 右子树是平衡的
* 左子树高度 - 右子树高度｜ <= 1

这些信息都依赖且仅依赖它的左右子结点。
所以如果这个结点可以拿到左右子结点给出的这些信息，就可以判断这颗子树是否是平衡的，
然后处理信息交给这个结点的父结点。

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ReturnType:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height
```