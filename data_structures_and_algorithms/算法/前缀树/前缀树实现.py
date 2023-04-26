'''前缀树，一个字符串类型的数组arr1，另一个字符串类型的数组arr2。arr2中有哪些字符是arr1中出现过的？'''
'''
    利用前缀树解决。
    【精准空降到 04:21】 https://www.bilibili.com/video/BV13g41157hK/?p=10&share_source=copy_web&vd_source=efc4a4eb35d298b244a48a32c9e1fb8b&t=261
    
    树的结点保存的信息是：
    1. 当前结点的通过次数
    2. 当前结点是某个字符串的结尾的次数
    3. 当前结点通向字符串的下一个字符的的路径
        a. 路径没有建立过会保存None
        b. 路径建立过，则保存通向下个字符的TrieNode
    
    字符种类很少的时候使用固定长的数组表示比较方便
    当字符种类很多的时候可以使用字典来表示“路径”，写函数的细节有所不同而已
    
    nexts中的对应位置就是路径信息：`head.next[0] is not None`意味着0：a的路径存在
    而在下一个结点才会保存这个a的经过信息pas和是否是字符串终点的信息end
'''

class TrieNode:
    def __init__(self, pas=0, end=0, nexts=None):
        # 当前结点的通过次数
        self.pas = pas
        # 当前结点是某个字符串的结尾的次数
        self.end = end

        # nexts[0] = None           没有走向a的路
        # nexts[15] = TrieNode()    有走向z的路
        if nexts is None:
            self.nexts = [None]*26

    def insert(self, word: str):
        '''
        向前缀树中加入字符串
        :param word:
        :return:
        '''
        l = [ord(word[i]) for i in range(len(word))]
        node = self
        node.pas += 1
        for i in range(len(word)):
            index = l[i] - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.pas += 1
        node.end += 1

    def search(self, word: str):
        '''
        查询一个单词之前在前缀树中被加入过几次
        :param word:
        :return:
        '''
        if word is None:
            return 0
        l = [ord(word[i]) for i in range(len(word))]
        node = self
        for i in range(len(word)):
            index = l[i] - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.end

    def prefix_number(self, word):
        '''
        加入的字符串中有几个字符串是以word作为前缀的？
        :param word:
        :return:
        '''
        if word is None:
            return 0
        l = [ord(word[i]) for i in range(len(word))]
        node = self
        for i in range(len(word)):
            index = l[i] - ord('a')
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.pas

    def delete(self, word):
        '''
        从前缀树中删除加入过的字符串
        必须先要检查是否已经加入过，不然会把以word为前缀的字符串的前缀word删除

        分两种情况：
        1. 删除这个字符串后本身路径不消失
        2. 删除这个字符串后路径消失（不然会减为负数）
        :param word:
        :return:
        '''
        # 如果前缀树里没有这个字符串就不做删除操作，直接返回
        if self.search(word) == 0:
            return
        l = [ord(word[i]) for i in range(len(word))]
        node = self

        # 删除沿途的pas信息
        for i in range(len(word)):
            index = l[i] - ord('a')
            node.nexts[index].pas -= 1

            # 如果下一个字符被删除后没有被经过，则要删除整个路径
            if node.nexts[index].pas == 0:
                # 有自动GC的语言可以这样直接释放内存，没有这种功能的语言，如cpp，就要手动遍历释放内存
                node.nexts[index] = None
                return

            node = node.nexts[index]

        node.end -= 1



head = TrieNode()
head.insert('abc')
head.insert('aedf')
num = head.search('aedf')
print(num)
num = head.prefix_number('a')
print(num)