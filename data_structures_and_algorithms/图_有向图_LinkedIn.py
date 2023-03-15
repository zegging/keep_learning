# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 图_有向图_LinkedIn.py
@time: 2022/12/9 16:45
@参考: 《数据结构与算法图解》 P134
"""

class Person(object):

    def __init__(self, name):
        self.name = str(name)
        self.friends = []
        self.visited = False
        # 0: 普通关注 1: 特殊关注
        self.follow = {}
        self.follower = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def add_friend(self, friend):
        '''
            这表示关系是无向的
        '''
        if type(friend) == Person:
            self.friends.append(friend)
            friend.friends.append(self)
        elif type(friend) == list:
            for each in friend:
                if type(each) == Person:
                    self.friends.append(each)
                    each.friends.append(self)
                else:
                    raise TypeError(f'unsupported type {each.__class__.__name__}, friend type must be Person')
        else:
            raise TypeError(f'unsupported type {friend.__class__.__name__}, friend type must be Person')

    def display_network(self):
        '''
            展示self的所有好友
        :return:
        '''
        to_reset = []
        queue = [self]
        self.visited = True

        while queue != []:
            cur_vertex = queue.pop(0)
            print(cur_vertex)

            for each in cur_vertex.friends:
                if each.visited != True:
                    to_reset.append(each)
                    queue.append(each)
                    each.visited = True

        for each in to_reset:
            each.visited = False

    def add_follow(self, follow, follow_type=0):
        '''
            关注person，是有向加权图
        :param follow:
        :return:
        '''
        if type(follow) == Person:
            self.follow.update({follow.name: follow_type})
            follow.follower.append(self)

if __name__ == '__main__':
    # name_list = ['Alice', 'Bob', 'Candy', 'Derek', 'Elaine', 'Fred', 'Gina', 'Helen', 'Irena']
    # names = locals()
    # for each in name_list:
    #     locals()[each] = Person(each)
    # print(Alice)

    alice = Person('Alice')
    bob = Person('Bob')
    candy = Person('Candy')
    derek = Person('Derek')
    elaine = Person('Elaine')
    fred = Person('Fred')
    gina = Person('Gina')
    helen = Person('Helen')
    irena = Person('Irena')

    alice.add_friend([bob, candy, derek, elaine])
    bob.add_friend(fred)
    derek.add_friend(gina)
    fred.add_friend(helen)
    gina.add_friend(irena)

    print(alice.friends)

    bob.display_network()

    alice.add_follow(bob)
    print(alice.follow)
    print(bob.follower)

