# 图的表示方法：
# 邻接表法（储存直接相连的点）、邻接矩阵法（储存边的信息）
# 表达图的方式多种多样，特殊的图需要将算法重新在这种结构上重新实现一遍
# 用一种自己喜欢的方式把图的算法的实现全都写一遍，做成一个转换的接口，将新的结构转化为自己熟悉的结构
import time


class Graph():
    '''
        the basic class of graph
    '''
    def __init__(self):
        self.nodes = set()
        self.edges = set()

    def createGraph(self):
        '''
        the API function to create a new graph
        :return:
        '''
        pass


class Node():

    def __init__(self, val: int, ind=0, outd=0):
        '''
        :param val: the value of node
        :param ind: the number of edges to this node
        :param outd: the number of edges from this node
        :param nexts: nodes which this node to
        :param edges: edges start from this node
        '''
        self.val = val
        self.ind = ind
        self.outd = outd
        self.nexts = set()
        self.edges = set()

    def __repr__(self):
        return str(self.val)

    def add_next_node(self, node, no_direction=True, **kwargs):
        # if not isinstance(node, Node):
        #     raise TypeError('node must be Node Type')
        if node not in self.nexts:
            self.nexts.add(node)
            self.outd += 1
            node.ind += 1
            if no_direction == False:
                edge = Edge(frm=self, to=node)
                self.edges.add(edge)
                node.edges.add(edge)

    def add_edge(self, edge):

        if edge.frm != self and edge.to != self:
            raise KeyError(f'{self} not in edge')

        if edge not in self.edges:
            if edge.frm == self:
                self.edges.add(edge)
                self.add_next_node(edge.to)
            if edge.to == self:
                self.edges.add(edge)
                edge.to.add_next_node(self)

class Edge():

    def __init__(self, frm, to, weight=0):
        '''

        :param weight: the weight of edge
        :param frm: the node which this edge from
        :param to: the node which this edge to
        '''
        self.weight = weight
        self.frm = frm
        self.to = to

    def __repr__(self):
        return f'from {self.frm} to {self.to} weight {self.weight}'

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.add_next_node(b)
a.add_next_node(c)
a.add_next_node(e)
c.add_next_node(b)
c.add_next_node(d)
c.add_next_node(a)
d.add_next_node(b)
d.add_next_node(c)
d.add_next_node(e)
e.add_next_node(a)
e.add_next_node(b)
e.add_next_node(d)

def bfs(node: Node):
    '''
    宽度优先遍历
    :return:
    '''
    queue = []
    visited = set()
    queue.insert(0, node)
    visited.add(node)
    while queue != []:
        cur = queue.pop()
        print(cur.val)
        for next in cur.nexts:
            if next not in visited:
                visited.add(next)
                queue.insert(0, next)

# bfs(a)

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.add_next_node(b)
a.add_next_node(c)
a.add_next_node(e)
b.add_next_node(a)
b.add_next_node(c)
c.add_next_node(b)
c.add_next_node(d)
c.add_next_node(a)
d.add_next_node(c)
d.add_next_node(e)
e.add_next_node(a)
e.add_next_node(d)
e.add_next_node(c)


# 深度优先遍历，递归形式 chatGPT版本
#
# 在这里，dfs函数是深度优先搜索的实现，它采用递归的方式遍历整个图。
# 对于给定的节点，函数首先将其添加到已访问的集合中，并打印节点的值。
# 然后，对于每个与该节点相邻的节点，如果它尚未被访问，就递归调用dfs函数来访问该节点。
#
# 最后，dfs_traversal函数是深度优先遍历的入口点，它接收一个节点列表nodes作为输入，该列表包含了整个图的所有节点。
# 该函数首先创建一个空的已访问集合visited，然后遍历图中的每个节点，如果该节点尚未被访问，就调用dfs函数来访问该节点及其所有可达节点。

# def dfs(node: Node, visited: set) -> None:
#     visited.add(node)
#     print(node.val)
#     for next_node in node.nexts:
#         if next_node not in visited:
#             dfs(next_node, visited)
#
# def dfs_traversal(nodes: list[Node]) -> None:
#     visited = set()
#     for node in nodes:
#         if node not in visited:
#             dfs(node, visited)
#
#
# # 记录函数开始时间
# start_time = time.time()
#
# # 调用函数
# dfs_traversal([a,b,c,d,e])
#
#
# # 记录函数结束时间
# end_time = time.time()
#
# # 计算函数的运行时间
# run_time = end_time - start_time
#
# print(run_time)

# 我们使用 deque 来代替列表来实现栈，并使用 continue 来避免在访问过的节点上进行重复操作。
# 我们还将访问节点的操作与推入未访问邻居节点的操作合并成一个循环，以进一步提高效率。

# 其实还是有所浪费，因为会出现下面这种情况。
# 随着图的复杂，一个点可能会被多次加入到队列中，造成浪费
# def dfs_traversal_iterative(node: Node) -> None:  node:1
#     visited = set()   visited: {1, 2}
#     stack = deque([node])     stack: deque{[3, 5, ,3]}
#     while stack:
#         cur_node = stack.pop()    cur_node: 2
#         if cur_node in visited:
#             continue
#         visited.add(cur_node)
#         print(cur_node.val)
#         for next_node in cur_node.nexts:  next_node: 1
#             if next_node not in visited:
#                 stack.append(next_node)
#
# from collections import deque
#
# def dfs_traversal_iterative(node: Node) -> None:
#     visited = set()
#     stack = deque([node])
#     while stack:
#         cur_node = stack.pop()
#         if cur_node in visited:
#             continue
#         visited.add(cur_node)
#         print(cur_node.val)
#         for next_node in cur_node.nexts:
#             if next_node not in visited:
#                 stack.append(next_node)


def dfs(node: Node):
    '''
    :param node:
    :return:
    '''
    stack = []
    visited = set()
    stack.append(node)
    visited.add(node)
    # 对node进行处理
    print(node.val)
    # 当深度遍历结束的时候stack中保存的是遍历的路径
    while stack:
        cur = stack.pop()
        for next in cur.nexts:
            if next not in visited:
                stack.append(cur)
                stack.append(next)
                visited.add(next)
                # 对遍历的新结点进行处理
                print(next.val)
                break

# dfs(a)

# 拓扑排序
# 参考：https://www.bilibili.com/video/BV13g41157hK/?p=9&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=3604
# 经常用在决定编译顺序的排序上：最开始应该编译哪个包，之后的编译顺序应该是什么？
# 重点在于找到入度为0的点（只在别的包中被import的包），注意，此时的图应该是没有环的，即不能循环编译。

def sortedTopology(graph: Graph):
    indMap = {} # 所有点的入度
    zeroIndQueue = [] # 入度为0的点才能进这个队列
    # 初始化indMap
    for node in graph.nodes:
        indMap.update({node, node.ind})
        if node.ind == 0:
            zeroIndQueue.insert(0, node)
    result = []
    while zeroIndQueue:
        cur = zeroIndQueue.pop()
        result.append(cur)
        for node in cur.nexts:
            indMap[node] = indMap[node]-1
            if indMap[node] == 0:
                zeroIndQueue.insert(0, node)
    if len(graph.nodes) != len(result):
        raise KeyError(f'graphy:{graph} should have no circle')
    return result














# # 记录函数开始时间
# start_time = time.time()
#
# # 调用函数
# dfs_traversal([a,b,c,d,e])
#
#
# # 记录函数结束时间
# end_time = time.time()
#
# # 计算函数的运行时间
# run_time = end_time - start_time
#
# print("函数的运行时间为：{:.2f}秒".format(run_time))




