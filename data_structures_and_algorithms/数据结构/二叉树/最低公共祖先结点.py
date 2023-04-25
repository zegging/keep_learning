class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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


'''
1）1是2或者2是1的最低公共祖先
2）1，2不互为最低公共祖先，向上汇聚才能找到
'''