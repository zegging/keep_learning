# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: 有向加权图最短路径算法.py
@time: 2022/12/10 15:55
@参考: 《数据结构与算法图解》 [美]杰伊•温格罗，袁志鹏译 P148
"""
class City(object):

    def __init__(self, name):
        self.name = str(name)
        self.routes = {}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def add_route(self, city, price):
        if type(city) == City:
            if type(price) == int:
                self.routes.update({city: price})
            else:
                raise TypeError('price type must be int')
        else:
            raise TypeError('city type must be City')

def route_price(start_city, other_cities):
    '''
    计算从开始城市到其他城市的最便宜的路程价格
    :param start_city:
    :param other_cities:
    :return:
    '''
    routes_from_city = {}
    routes_from_city[start_city] = [0, start_city]
    for city in other_cities:
        routes_from_city[city] = [float('inf')]
    visited_city = []
    cur_city = start_city
    while cur_city:
        visited_city.append(cur_city)
        for city, price in cur_city.routes.items():
            if routes_from_city[city][0] > price + routes_from_city[cur_city][0]:
                routes_from_city[city][0] = price + routes_from_city[cur_city][0]
                routes_from_city[city].append(cur_city)
        cur_city = None
        cheapest_route_from_current_city = float('inf')
        for city, price in routes_from_city.items():
            if city not in visited_city and price[0] < cheapest_route_from_current_city:
                cur_city = city
                cheapest_route_from_current_city = price[0]
    return routes_from_city

if __name__ == '__main__':
    denver = City('Denver')
    el_paso = City('El Paso')
    chicago = City('Chicago')
    boston = City('Boston')
    atlanta = City('Atlanta')

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)
    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)
    chicago.add_route(el_paso, 80)
    denver.add_route(chicago, 40)
    denver.add_route(el_paso, 140)

    print(route_price(atlanta, [denver, el_paso, chicago, boston]))


