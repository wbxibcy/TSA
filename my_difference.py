import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False 

def multi_order_difference(data, order):
    '''
    多阶差分函数

    参数：
    data: list, 时间序列数据
    order: int, 差分的阶数

    返回：
    diff_data: list, 差分后的数据
    '''
    if order <= 0:
        return data
    diff_data = data
    for i in range(order):
        diff_data = [diff_data[j] - diff_data[j-1] for j in range(1, len(diff_data))]
    return diff_data

data = np.array([1, 4, 6, 8, 12, 15, 20])
order = 2
# 多阶差分
diff_data = multi_order_difference(data, order)
print(diff_data)

plt.figure(figsize=(8, 4))
plt.subplot(2, 1, 1)
plt.plot(data, marker='o')
plt.title('原始数据')
plt.subplot(2, 1, 2)
plt.plot(diff_data, marker='o')
plt.title(f'{order}阶差分后的数据')
plt.tight_layout()
plt.show()
