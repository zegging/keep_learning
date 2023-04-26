'''滑动窗口 LC 3.无重复字符的最长子串'''

'''
    滑动窗口是一种想象出来的数据结构
    窗口有左边界L和右边界R
    在一个序列S上，窗口就是是 S[L:R] 这一部分
    L向右滑动意味着一个样本出了窗口，R向右滑东意味着一个样本进了窗口
    L、R都只能向右滑，且 L <= R
    
    最开始L、R都指向序列的起始位置前（窗口中不包含任何一个S中的元素）
    
    【窗口左右位置】
    
    【代表窗口状况的双端队列】
    
    双端队列中内容的含义是：当L向右移动后代表新的窗口状况的优先级
'''

'''
    设定一个固定大小为W的窗口，依次划过arr
    返回每一次滑出状况的最大值
    arr = [4,3,5,4,3,3,6,7] W = 3
    return [5,5,5,4,6,7]
'''

def getMaxWindow(arr, W):
    res = []
    # 双端队列中保存位置信息，头部所代表的数是从大到小到尾部的
    queue = []

    # 不停让 arr[R] 进入窗口
    for R in range(len(arr)):
        if queue == []:
            queue.append(R)
        else:
            # 当双端队列的尾部比 arr[R] 小的时候就弹出
            while queue != [] and arr[queue[-1]] < arr[R]:
                queue.pop()
            # 将 R 加入双端队列尾部，之前的数字作为index，arr[index] >= arr[R]
            queue.append(R)

        # R位置进入窗口，过期位置的下标是 R-W
        # 如果双端队列中的第一个位置的数是应该被弹出的index，就弹出
        if queue[0] == R - W:
            del queue[0]

        if R >= W-1:
           res.append(arr[queue[0]])

    return res

res = getMaxWindow([4,3,5,4,3,3,6,7], 3)
print(res)






