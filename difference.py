import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False 

def multi_diff(arr, order):
    '''
    多阶差分函数

    参数:
    data: 时间序列数据
    order: 差分的阶数

    返回:
    result: numpy数组, 多阶差分后的数据
    '''
    result = arr
    for i in range(order):
        result = np.diff(result)
    return result

data = np.array([1, 4, 6, 8, 12, 15, 20])

order = 2  # 差分阶数
result = multi_diff(data, order)
print(result)
