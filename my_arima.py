import numpy as np
import pandas as pd
import statsmodels.api as sm

def estimate_ar_coefficients(data, p):
    """
    最小二乘法估计AR模型的系数

    参数：
    data: list or np.array, 输入数据
    p: int, AR阶数

    返回：
    ar_coefs: np.array, AR模型的系数
    """

    n = len(data)
    X = np.zeros((n-p, p))
    y = np.array(data[p:])
    
    # 构造自回归矩阵X
    for i in range(n-p):
        X[i, :] = data[i:i+p]

    # 最小二乘法拟合AR模型
    ar_coefs = np.linalg.lstsq(X, y, rcond=None)[0]

    return ar_coefs

def estimate_ma_coefficients(residuals, q):
    """
    最小二乘法估计平均移动模型的参数

    参数:
    residuals: 时间序列的残差
    q: 平均移动模型的阶数

    返回值:
    参数估计值
    """

    mask = ~np.isnan(residuals)
    residuals = np.interp(np.arange(len(residuals)), np.arange(len(residuals))[mask], residuals[mask])

    n = len(residuals)
    print(n)

    X = np.zeros((n-q, q))
    y = np.array(residuals[q:])
    
    # 构造自回归矩阵X
    for i in range(n-q):
        X[i, :] = residuals[i:i+q]

    # 最小二乘法求解参数估计值
    ma_coefs = np.linalg.lstsq(X, y, rcond=None)[0]

    return ma_coefs


def my_arima(data, p, d, q):
    """
    ARIMA模型拟合

    参数：
    data: list or np.array, 输入的时间序列数据
    p: int, AR阶数
    d: int, 差分次数
    q: int, MA阶数

    返回：
    ar_coefs: np.array, AR模型的系数
    ma_coefs: np.array, MA模型的系数
    """

    # 差分处理
    diff_data = data
    for i in range(d):
        diff_data = np.diff(diff_data)

    # 残差
    result = sm.tsa.seasonal_decompose(data, model='additive')
    residual = result.resid
    # print(len(residual))
    # print(residual[:10])
    
    # 拟合ARIMA模型
    ar_coefs = estimate_ar_coefficients(diff_data, p)
    ma_coefs = estimate_ma_coefficients(residual, q)

    return ar_coefs, ma_coefs


np.random.seed(42)
seasonal_data = np.sin(np.linspace(0, 4 * np.pi, 100)) + np.random.normal(0, 0.5, 100)
time_index = pd.date_range(start='2023-01-01', periods=100, freq='M')
data = pd.Series(seasonal_data, index=time_index)

# 阶数
p, d, q = 2, 1, 2

# 拟合ARIMA模型
ar_coefs, ma_coefs = my_arima(data, p, d, q)

print("AR模型的系数: ", ar_coefs)
print("MA模型的系数: ", ma_coefs)
