import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False 

def plot_acf_pacf(time_series, lags=20):
    '''
    绘制acf和pacf图
    
    参数:
    time_series: pd.Series, 时间序列数据
    滞后阶数: int, 滞后阶数的值, 默认是20
    '''
    acf_values = sm.tsa.acf(time_series, nlags=lags)
    pacf_values = sm.tsa.pacf(time_series, nlags=lags)

    # ACF and PACF
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plot_acf(time_series, lags=lags, ax=plt.gca(), title="ACF")
    plt.subplot(2, 1, 2)
    plot_pacf(time_series, lags=lags, ax=plt.gca(), title="PACF")
    plt.tight_layout()
    plt.show()

np.random.seed(42)
data = np.random.randn(100) 
time_series = pd.Series(data)

plot_acf_pacf(time_series, lags=20)