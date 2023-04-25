def KMP(s1, s2):
    if s1 == '' or s2 == '' or len(s2) == 0 or len(s1) < len(s2):
        return -1
    i1 = 0
    i2 = 0
    next = get_next_arr(s2)
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        elif i2 == 0:
            i1 += 1
        else:
            i2 = next[i2]
    # 如果 i2 == len(s2) 意味着while循环是因为 i2 = len(s2) 退出的
    # 这意味着s2被完全匹配出来了，所以返回s1中匹配s2的起始位置
    # 否则返回-1
    return i1 - i2 if i2 == len(s2) else -1

def get_next_arr(s):
    if len(s) == 1:
        return [-1]
    next = [0]* len(s)
    next[0] = -1
    next[1] = 0
    i = 2
    cn = 0
    while i < len(s):
        if s[i-1] == s[cn]:
            next[i] = cn+1
            i += 1
            cn += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[i] = 0
            i += 1
    return next

s1 = '123abcdeab'
s2 = 'ab'

print(KMP(s1,s2))


