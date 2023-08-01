import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False 

def acf(time_series, lags=20):
    """
    计算时间序列的自相关函数（ACF）。

    参数：
    time_series: pd.Series, 时间序列数据
    lags: int, 滞后阶数的值, 默认为20

    返回：
    acf_values: list, ACF值
    """
    n = len(time_series)
    mean = time_series.mean()
    variance = time_series.var()
    acf_values = []
    for lag in range(lags + 1):
        cov = sum((time_series[i] - mean) * (time_series[i - lag] - mean) for i in range(lag, n))
        acf_values.append(cov / variance)
    return acf_values

def pacf(time_series, lags=20):
    """
    计算时间序列的偏自相关函数（PACF）。

    参数：
    time_series: pd.Series, 时间序列数据
    lags: int, 滞后阶数的值, 默认为20

    返回：
    pacf_values: list, PACF值
    """
    n = len(time_series)
    pacf_values = [1.0]
    for k in range(1, lags + 1):
        coefficients = np.polyfit(time_series.index, time_series, k)
        residuals = time_series - np.polyval(coefficients, time_series.index)
        pacf_values.append(np.corrcoef(residuals[k:], residuals[:-k])[0, 1])
    return pacf_values

def plot_acf_pacf(time_series, lags=20):
    """
    绘制时间序列的ACF和PACF图。

    参数：
    time_series: pd.Series, 时间序列数据
    lags: int, 滞后阶数的值, 默认为20

    返回：
    None
    """
    acf_values = acf(time_series, lags)
    pacf_values = pacf(time_series, lags)

    # 绘制ACF和PACF图
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.stem(range(len(acf_values)), acf_values, use_line_collection=True)
    plt.title("ACF")
    plt.subplot(2, 1, 2)
    plt.stem(range(len(pacf_values)), pacf_values, use_line_collection=True)
    plt.title("PACF")
    plt.tight_layout()
    plt.show()

np.random.seed(42)
data = np.random.randn(100) 
time_series = pd.Series(data)

plot_acf_pacf(time_series, lags=20)
