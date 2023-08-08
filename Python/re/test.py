# -*- coding: utf-8 -*-

"""
@author: huiti
@software: PyCharm
@file: test.py
@time: 2022/9/26 10:34
"""
import re
source_1 = '''
the the thethe 11 11 22 3 22 111111 4 4 4
'''
pattern = re.compile(r'(.+) \1 ')
lst = re.findall(pattern , source_1)
for each in lst:
    print(each)
print('---------------------')

source_2 = 'agfhqui23y895125kjlC'
pattern = re.compile(r'\A ')
lst = re.findall(pattern , source_2)
for each in lst:
    print(each)
print('---------------------')

source_3 = '''hi hill, 889hi87 hihihi,hi, hi.（（（hi
'''
pattern = re.compile(r'hi')
p_1 = re.compile(r'\bhi')
p_2 = re.compile(r'\bhi\b')
lst = re.findall(pattern , source_3)
print(lst)          # 所有的hi
lst_1 = re.findall(p_1 , source_3)
print(lst_1)        # 所有的前没有Unicode字母，数字或下划线的hi
lst_2 = re.findall(p_2, source_3)
print(lst_2)        # 所有前后都没有Unicode字母，数字或下划线的hi
print('---------------------')

source_4 = '''a我，aa（（_awef。11abc cdef aghijk,bb225,a1111
'''
pattern = re.compile(r'a\w')
lst = re.findall(pattern , source_4)
print(lst)

pattern = re.compile(r'a\w*')
lst_1 = re.findall(pattern , source_4)
print(lst_1)

pattern = re.compile(r'\wa\w*')
lst_2 = re.findall(pattern , source_4)
print(lst_2)

pattern = re.compile(r'\w*a\w*')
lst_3 = re.findall(pattern , source_4)
print(lst_3)

print('---------------------')

source_3 = '''hi hill, 889hi87 hihihi,hi, hi.（（（hi
'''
pattern = re.compile(r'hi')
p_1 = re.compile(r'\Bhi')
p_2 = re.compile(r'\Bhi\B')
lst = re.findall(pattern , source_3)
print(lst)          # 所有的hi
lst_1 = re.findall(p_1 , source_3)
print(lst_1)        # 所有的前有Unicode字母，数字或下划线的hi
lst_2 = re.findall(p_2, source_3)
print(lst_2)        # 所有前后都有Unicode字母，数字或下划线的hi

print('--------------------------------------------------')
source_5 = '''九千一百八十六 玖千壹佰捌拾陆 9186 ⅠⅡ Ⅵ。九十9186'''
pattern = re.compile(r'\d+')
lst = re.findall(pattern, source_5)
print(lst)

print('--------------------------------------------------')
source_5 = '''九千一百八十六 玖千壹佰捌拾陆 9186 ⅠⅡ Ⅵ。九十9186'''
pattern = re.compile(r'\D+')
lst = re.findall(pattern, source_5)
print(lst)

print('--------------------------------------------------')
source_6 = '''九千一百八十六 玖千壹\t佰捌拾陆 9186 
ⅠⅡ Ⅵ。\n 九十9186'''
pattern = re.compile(r'\s')
lst = re.findall(pattern, source_6)
print(lst)

print('--------------------------------------------------')
source_6 = '''九千一百八十六 玖千壹\t佰捌拾陆 9186 
ⅠⅡ Ⅵ。\n 九十9186'''
pattern = re.compile(r'\S+')
lst = re.findall(pattern, source_6)
print(lst)

print('--------------------------------------------------')
source_7 = '''abcbd'''
pattern = re.compile(r'a[bcd]*b')
lst = re.findall(pattern, source_7)
print(lst)

print('--------------------------------------------------')
source_8 = '''From Here to Eternity, 
From Reciting From Memory'''
print(source_8)
pattern_1 = re.compile(r'^From',re.M)
lst_1 = re.findall(pattern_1, source_8)
print(lst_1)
pattern_2 = re.compile(r'^From')
lst_2 = re.findall(pattern_2, source_8)
print(lst_2)

print('--------------------------------------------------')
source_9 = '''{block}\n
{block} 
{block}'''
print(source_9)
pattern_1 = re.compile(r'}$',re.M)
lst_1 = re.findall(pattern_1, source_9)
print(lst_1)
pattern_2 = re.compile(r'}$')
lst_2 = re.findall(pattern_2, source_9)
print(lst_2)

print('--------------------------------------------------')
source_10 = ''''no class at all, the declassified algorithm. one subclass is'''
pattern = re.compile(r'\bclass\b')
lst = re.findall(pattern, source_10)
print(lst)

print('--------------------------------------------------')
source_10 = ''''no class at all, the declassified algorithm. one subclass is'''
pattern = re.compile('\bclass\b')
print('\bclass\b')
lst = re.findall(pattern, source_10)
print(lst)

print('--------------------------------------------------')
pattern = re.compile(r'\Bclass\B')
lst = re.findall(pattern, source_10)
print(lst)

print('--------------------------------------------------')
source_11 = '''abcd'''
pattern = re.compile(r'(a(b)c)d')
m = re.match(pattern, source_11)
print(m)
print(m.group(), m.group(0), m.group(1), m.group(2))
pattern = re.compile(r'(a(b)c)d')
m = re.match(pattern, source_11)
print(m)
print(m.group(), m.group(0), m.group(1), m.group(2))

print('--------------------------------------------------')
source_11 = '''abcd'''
pattern = re.compile(r'(a(b)c)d')
lst = re.findall(pattern, source_11)
print(lst)

print('--------------------------------------------------')
source_12 = '''abc'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, source_12)
print(m.group(), m.group(1))
lst = re.findall(pattern, source_12)
print(lst)

source_12 = '''abcd'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, source_12)
print(m.group(), m.group(1))
lst = re.findall(pattern, source_12)
print(lst)

print('--------------------------------------------------')
source_13 = '''2022-09-26'''
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
lst = re.findall(pattern, source_13)
print(lst)
pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
lst = re.findall(pattern, source_13)
print(lst)
m = re.match(pattern, source_13)
print(m.group(), m.group(1), m.group(2), m.group(3))

pattern = re.compile(r'(?:\d{4})-(?:\d{2})-(?:\d{2})')
lst = re.findall(pattern, source_13)
print(lst)
m = re.match(pattern, source_13)

# print(m.group(), m.group(1))
# IndexError: no such group

print('------------------------------------------------------------------')
source = '''news.rc
weibo.com
baidu.com
bnu.edu
sample.batch
sendmail.cf
autoexec.bat
foo.bar
'''
pattern = re.compile(r'.*[.].*$', re.M)
lst = re.findall(pattern, source)
print(lst)

print('------------------------------------------------------------------')
source = '''news.rc
weibo.com
baidu.com
bnu.edu
sample.batch
sendmail.cf
autoexec.bat
exa.
foo.bar
'''
pattern = re.compile(r'.*[.](?!bat$)[^.\n]+$', re.M)
lst = re.findall(pattern, source)
print(lst)

print('---------------------------------------')
source = '''This is a car, that is a fat cat. '''
pattern = re.compile(r'a(?=r)')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'a(?=t)')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'a(?=r|t)')
lst = re.findall(pattern, source)
print(lst)


print('---------------------------------------')
source = '''This is a car, that is a fat cat. '''
pattern = re.compile(r'(?=c)a')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'(?:c)a')
lst = re.findall(pattern, source)
print(lst)

# pattern = re.compile(r'a(?=t)')
# lst = re.findall(pattern, source)
# print(lst)
# pattern = re.compile(r'a(?=r|t)')
# lst = re.findall(pattern, source)
# print(lst)

print('----------------------------------------')
source = '''
sjoop$jhfa-j@
'''
pattern = re.compile(r'''
[$-@]*                              
'''
, re.VERBOSE)
lst = re.findall(pattern, source)
print(lst)

print('----------------------------------------')
source = '''
http://test.cn
www.baidu.com
google.com哈哈哈
jjj.osiuf
nihao.www.ad/api/helo
nihao.www.adsgjaki
邮箱672502172@qq.com
http://17.5cm/\
http://17.5cm
http://0.85mps/
http://0.05mpa/
http://10.154.55.13/
http://2.0.0.5/\
http://image.meilele.、
http://image.me.
'''
pattern = re.compile(r'''
(?:(?:http[s]?|ftp)://)?        
(?:[a-zA-Z0-9_-]+[.]|[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+)+
(?:aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cx|cy|cz|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mn|mo|mp|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|nom|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ra|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw|arpa) 
(?!\w)
(?:/(?:[a-zA-Z]|[0-9]|[$-_@.&+#:%_~=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*)*                          
'''
, re.VERBOSE)
lst = re.findall(pattern, source)
print(lst)



# p = re.compile(r'''
# (?:http[s]?://|ftp://)?         # 传输协议
# (?!
#     (?:[0-9]*[.][0-9]*[mm|cm|m|mg|g|kg|l|L]/)
#     |(?:[0-9]*[.][0-9]*[.][0-9]*[.][0-9]*/)
#     )
# (?:[a-zA-Z]
#     |[0-9]
#     |[$-_@.&+#:%_~=]
#     |[!*\(\),]
#     |(?:%[0-9a-fA-F][0-9a-fA-F])
#     )+                                 # http, https, sample. 后续有字符
#
# '''
# , re.VERBOSE)







#
# p = re.compile('[a-z]+')
# print(p)
# m = p.match('love')
# print(m)

print('-----------------------------------------------------------')
source = '''
'''
pattern = re.compile(r'abcd')
print(pattern, type(pattern))

print('-----------------------------------------------------------')
source = '''aT cdhhuTTogTTTTooTgg
'''
pattern = re.compile(r'T')
position = pattern.search(source)
print(position)
pattern = re.compile(r'TT')
position = pattern.search(source)
print(position)
pattern = re.compile(r'TTT')
position = pattern.search(source)
print(position)
pattern = re.compile(r'A')
position = pattern.search(source)
print(position)
pattern = re.compile(r'$')
position = pattern.search(source)
print(position)
pattern = re.compile(r'a')
position = pattern.search(source)
print(position)
pattern = re.compile(r'a')
position = pattern.search(source, 1)
print(position)


print('-----------------------------------------------------------')
source = '''aTT cdhhuTTogTTTTooTgg
'''
pattern = re.compile(r'TT')
position = re.match(pattern, source)
print(position)
pattern = re.compile(r'\b')
position = re.match(pattern, source)
print(position)

print('----------------------------------------------------------------')
l_1 = re.split(r'\W+', 'Words, words, words.')
l_2 = re.split(r'(\W+)', 'Words, words, words.')
l_3 = re.split(r'\W+', 'Words, words, words.', 1)
l_4 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
l_5 =  re.split(r'(\W+)', '...words, words...')
print(l_1)
print(l_2)
print(l_3)
print(l_4)
print(l_5)

print('----------------------------------------------')
l_1 = re.split(r'\b', 'Words, words, words.')
l_2 = re.split(r'\W*', '...words...')
l_3 = re.split(r'(\W*)', '...words...')
print(l_1)
print(l_2)
print(l_3)



print('----------------------------------------------')
l_1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell faster')
l_2 = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(l_1)
print(l_2)

print('----------------------')
l = re.finditer(r'\bf[a-z]*', 'which foot or hand fell faster')
print(l)

print('--------------------------------------')
l = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
           r'static PyObject*\npy_\1(void)\n{',
           'def myfunc():')
print(l)

l_1 = re.sub(r'(\S[^的]*)的(\S[^是]*)是(\S[^?]*)？',
             r'\1的\2是曹操',
             '曹丕的父亲是谁？')
print(l_1)

l_2 = re.sub(r'(\S[^和]*)和(\S[^和]*)是邻国？',
             r'\1和\2接壤',
             r'中国和俄罗斯是邻国？')
print(l_2)


print('--------------------------------------------------')
string = '''abc'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, string)
print(m.group(), m.group(1))
lst = re.findall(pattern, string)
print(lst)

string = '''abca'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, string)
print(m.group(), m.group(1))
lst = re.findall(pattern, string)
print(lst)

string = '''abc'''
pattern = re.compile(r'([abc])([abc])([abc])')
m = re.match(pattern, string)
print(m.group(), m.group(1), m.group(2), m.group(3))
lst = re.findall(pattern, string)
print(lst)

string = 'abc123'
pattern = re.compile(r'([abc])+([123])+')
m = re.match(pattern, string)
print(m.group(), m.group(1), m.group(2))
lst = re.findall(pattern, string)
print(lst)


# source_12 = '''abcdc'''
# pattern = re.compile(r'([abc])+')
# m = re.match(pattern, source_12)
# print(m.group(), m.group(1))
# lst = re.findall(pattern, source_12)
# print(lst)

print('----------------------------------------------')
# def dashrepl(matchobj):
#     if matchobj.group(0) == '-': return ' '
#     else: return '-'
# print(re.compile(r'(-{1,2})').split('pro----gram-files'))
# l_f = re.compile(r'(-{1,2})').findall('pro----gram-files')
# print(l_f)
# l = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
# print(l)


def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
l = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
print(l)


print('----------------------------------------')
pattern = re.compile(r'x*')
l = re.subn('x*', '-', 'abxd')
print(l)
l = re.subn('x*', '-', '  abxd')
print(l)

print('-------------------------------------------------')
str = '123456'
pattern = re.compile('\d+')
str_1 = pattern.pattern
print(id(str), id(pattern), id(str_1))

print('-------------------------------------')
m = re.match(r'(\d+)', '123\n*zbv*')
print(m.expand(r'是以数字开头的字符串，数字为：\1'))

print('--------------------------------------------')
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.groups())
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name'))
print(m.group('last_name'))

m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times
print(m.group(1))


m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m[1])


print('-------------------------------------------')
m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())

m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
print(m.groups('0'))



m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())