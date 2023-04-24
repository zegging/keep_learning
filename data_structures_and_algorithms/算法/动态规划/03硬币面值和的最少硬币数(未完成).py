# 一共有N枚硬币                               [2,7,3,5,3]
# 每一枚有一个面值，面值可能重复                 arr = []
# 选取硬币使得面值和为S，求最少用多少枚硬币         S = 10


def f1(arr, index, rest):
    '''

    :param arr:
    :param index: 当前硬币的索引
    :param rest:
    :return:
    '''
    if rest < 0:
        return -1
    if rest == 0:
        return 0
    # rest > 0
    if index == len(arr):
        return -1

    p1 = f1(arr, index+1, rest)
    p2 = f1(arr, index+1, rest-arr[index])

    if p1 == -1 and p2 == -1:
        return -1

    else:
        if p1 == -1:
            return p2+1
        if p2 == -1:
            return p1

    return min(p1, p2+1)

arr = [2,7,3,5,3]
res = f1(arr, 0, 10)
print(res)
