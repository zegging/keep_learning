# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@project: data_structures_and_algorithms
@file: test.py
@time: 2022/12/12 15:38
"""

from xeger import Xeger
import re

def generate_soa_api_pattern(string):
    '''
        soa搜索需要的pattern都是需要模拟真实url的
        类似：
            /api/page/cloud/decoproduct/model/{type:(?:dcatid|catid)}{catIdStr}
            /designpic/{obsDesignId:3(?:F|f)\w{10}}/{roomId:\w+}
        这样的url需要被改造成：
            /api/page/cloud/decoproduct/model/dcatidasdf564
            /designpic/3F12345678/adg45dsfa
    '''
    def change_content(content):
        pattern = re.compile(r'''
        (?:
            (?:(?<!}){[a-zA-Z]*})+          # delete /{catIdStr}123{catIdStr}, {catIdStr}{catIdStr} -> [^/]*[^/]*
           | (?:(?<=}){[a-zA-Z]*})+         # delete {type:(?:dcatid|catid)}{catIdStr}                 
        )''', re.VERBOSE)
        content = re.sub(pattern, r'[^/\\s\\W]*', content) # 防止在xeger()随机生成的时候生成\s和\W
        print(content)
        # delete {roomId:\w+}
        pattern = re.compile(r'''
        (?:{[a-zA-Z]+:([^/}]*)})
        ''', re.VERBOSE)
        content = re.sub(pattern, r'\1', content)
        print(content)
        # repl **
        pattern = re.compile(r'/[*]+')
        content = re.sub(pattern, r'/.*', content)
        print(content)
        return content

    x = Xeger(limit=10)
    res = x.xeger(change_content(string))
    print(res)
    res = re.sub(re.compile(r'(\s+|[^0-9a-zA-Z-/_])'), r'', res) # 去除替换可能生成的\s和非url可用字符
    return res

api = generate_soa_api_pattern('/vc/commodity/{t:(?:model)|(?:material)|(?:paving)|(?:lineandwall)|(?:coating)|(?:cupboard)|(?:wardrobe)|(?:doorwindow)|(?:group)}')

print(api)

if __name__ == '__main__':
    while True:
        try:
            l = 'afjdsihfahegf123905ru iewrj'
            for i in range(0, len(l), 8):
                print("{0:0<8s}".format(l[i:i + 8]))
        except:
            break
        break
