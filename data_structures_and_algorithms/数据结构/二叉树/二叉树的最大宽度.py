'''
求一颗二叉树的最大宽度（不包括None）
不同于leetcode 662. https://leetcode.cn/problems/maximum-width-of-binary-tree/
'''

def widthOfTree1(root):
    '''
    使用字典保存行号信息
    :param root:
    :return:
    '''
    if root == None:
        return 0
    queue = []
    queue.insert(0, root)
    levalMap = {}
    levalMap[root] = 1
    curLevel = 1
    curLevelNodes = 0
    m = 0
    while queue != []:
        cur = queue.pop()
        curNodeLevel = levalMap[cur]
        if curNodeLevel == curLevel:
            curLevelNodes += 1
        else:
            m = max(m, curLevelNodes)
            curLevel += 1
            curLevelNodes = 1
        if cur.left != None:
            levalMap[cur.left] = curNodeLevel+1
            queue.insert(0, cur.left)
        if cur.right != None:
            levalMap[cur.right] = curNodeLevel+1
            queue.insert(0, cur.right)
    return max(m, curLevelNodes)

def widthOfTree2(root):
    '''
    使用队列
    :param root:
    :return:
    '''
    if root == None:
        return 0
    curLevelEnd = root
    nextLevelEnd = None
    curLevelNodes = 0
    Max = 0
    queue = []
    queue.insert(0, root)
    while queue != []:
        cur = queue.pop()
        curLevelNodes += 1
        if cur.left != None:
            queue.insert(0, cur.left)
            nextLevelEnd = cur.left
        if cur.right != None:
            queue.insert(0, cur.right)
            nextLevelEnd = curLevelEnd.right
        if cur == curLevelEnd:
            Max = max(curLevelNodes, Max)
            curLevelEnd = nextLevelEnd
            curLevelNodes = 0
    return Max


'''
leetcode 662. https://leetcode.cn/problems/maximum-width-of-binary-tree/

'''
# class Solution:
#     def widthOfBinaryTree(self, root) -> int:
#