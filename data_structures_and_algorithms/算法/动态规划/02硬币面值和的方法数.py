# 一共有N枚硬币                               [2,7,3,5,3]
# 每一枚有一个面值，面值可能重复                 arr = []
# 选取硬币使得面值和为S，求可能的方法数M          S = 10
'''

'''

'''
暴力递归
先确定和为S的选法
'''

def s_S1(S, arr, index, pre):
    '''
    :param S: 目标面值和
    :param arr: 硬币列表
    :param index: 现在需要选择是否选取的硬币的索引
    :param pre: 已经选择的硬币面值之和
    :return: 方法总数
    '''
    if index == len(arr):
        return 1 if pre == S else 0

    # 不选择index这枚硬币和选择index这枚硬币能够使得面值和为S的方法总数
    return s_S1(S, arr, index+1, pre) + s_S1(S, arr, index+1, pre+arr[index])

count = s_S1(10, [2,7,3,5,3], 0, 0)
print(count)

print('---------------------------------------------------------------')

'''
记忆化搜索
'''

def init_dp1(arr):
    '''
    :param arr: 硬币列表
    :return: 缓存二维数组
    '''
    arr_total = 0
    for each in arr:
        arr_total += each
    # 所有硬币的最大和为arr_total，保证pre取值时不会超出列表范围
    dp = [[-1 for _ in range(arr_total+1)] for _ in range(len(arr))]
    return dp

def s_S2_1(S, arr, index, pre, dp):
    '''
    :param S: 目标面值和
    :param arr: 硬币列表
    :param index: 现在需要选择是否选取的硬币的索引
    :param pre: 已经选择的硬币面值之和
    :param dp: 缓存dp
    :return: 方法总数
    '''
    # 递归边界条件：
    # 如果 index == len(arr) 则arr中的硬币是否选取都已经确定了，那么pre就是这种选取方案下的面值之和
    # 如果 pre == S，那么这就是一种成功的方案，在dp中做缓存
    if index == len(arr):
        dp[index-1][pre] = 1 if pre == S else 0
        return dp[index-1][pre]

    # 如果dp中已经有缓存，则直接使用缓存数据
    if dp[index][pre] != -1:
        return dp[index][pre]

    # 没有缓存的话进行计算，(index, pre)情况下继续选择的方法数等于【选取index】和【不选取index】两种情况的和
    dp[index][pre] = s_S2_1(S, arr, index+1, pre, dp) + s_S2_1(S, arr, index+1, pre+arr[index], dp)
    return dp[index][pre]

arr = [2,7,3,5,3]
dp = init_dp1(arr)
count = s_S2_1(10, arr, 0, 0, dp)
print(count)

print('---------------------------------------------------------------')


'''
记忆化搜索还能继续优化，因为pre超出S时显然是不能满足的方案，可以直接返回
'''

def init_dp2(S, arr):
    '''
    :param S: 目标面值和
    :param arr: 硬币列表
    :return: 缓存二维数组
    '''
    arr_total = 0
    for each in arr:
        arr_total += each
    # 所有硬币的最大和为arr_total，保证pre取值时不会超出列表范围
    dp = [[-1 for _ in range(S+1)] for _ in range(len(arr))]
    return dp

def s_S2_2(S, arr, index, pre, dp):
    '''
    :param S: 目标面值和
    :param arr: 硬币列表
    :param index: 现在需要选择是否选取的硬币的索引
    :param pre: 已经选择的硬币面值之和
    :param dp: 缓存dp
    :return: 方法总数
    '''
    # 递归边界条件：
    # 如果 index == len(arr) 则arr中的硬币是否选取都已经确定了，那么pre就是这种选取方案下的面值之和
    # 如果 pre == S，那么这就是一种成功的方案，在dp中做缓存
    if index == len(arr):
        # 已经拥有的面值之和超出S，返回可能的方法数为0
        if pre > S:
            return 0
        else:
            dp[index-1][pre] = 1 if pre == S else 0
            return dp[index-1][pre]

    # 已经拥有的面值之和超出S，返回可能的方法数为0
    if pre > S:
        return 0

    # 如果dp中已经有缓存，则直接使用缓存数据
    if dp[index][pre] != -1:
        return dp[index][pre]

    # 没有缓存的话进行计算，(index, pre)情况下继续选择的方法数等于【选取index】和【不选取index】两种情况的和
    dp[index][pre] = s_S2_2(S, arr, index+1, pre, dp) + s_S2_2(S, arr, index+1, pre+arr[index], dp)
    return dp[index][pre]

arr = [2,7,3,5,3]
dp = init_dp2(10, arr)
count = s_S2_2(10, arr, 0, 0, dp)
print(count)


print('---------------------------------------------------------------')

'''
动态规划
'''
def s_S3(S, arr):
    dp = [[0 for _ in range(S+1)] for _ in range(len(arr)+1)]
    for each in dp:
        each[S] = 1

    line = 4
    while line >= 0:
        row = 0
        while row <= S:
            if row + arr[line] <= S:
                dp[line][row] = dp[line + 1][row] + dp[line + 1][row + arr[line]]
            else:
                dp[line][row] = dp[line + 1][row]
            row += 1
        line -= 1
    return dp[0][0]

arr = [2,7,3,5,3]
count = s_S3(10, arr)
print(count)

'''  
     0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10
2 0 [4, 0, 0, 1, 0, 1, 0, 2, 1, 0, 1]
7 1 [2, 0, 2, 1, 0, 1, 0, 2, 0, 0, 1]
3 2 [0, 0, 2, 0, 1, 1, 0, 2, 0, 0, 1]
5 3 [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
3 4 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
  5 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
  
  实际上line = 0 除了 row = 0 需要求值外其他值是可以不用求的，可以继续优化
'''
