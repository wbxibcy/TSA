import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
plt.rcParams["font.sans-serif"]=["SimHei"] 
plt.rcParams["axes.unicode_minus"]=False 

def seasonal_decompose_plot(time_series, model):
    '''
    季节性分解并绘制原始数据、趋势、季节性和残差

    参数:
    time_series: pd.Series 时间序列数据
    model: string 季节性分解的模型

    返回值:
        无
    '''
    result = sm.tsa.seasonal_decompose(time_series, model=model)

    trend = result.trend
    seasonal = result.seasonal
    residual = result.resid

    plt.figure(figsize=(12, 8))
    plt.subplot(4, 1, 1)
    plt.plot(time_series, label='原始时间序列')
    plt.legend(loc='upper left')
    plt.subplot(4, 1, 2)
    plt.plot(trend, label='趋势')
    plt.legend(loc='upper left')
    plt.subplot(4, 1, 3)
    plt.plot(seasonal, label='季节性')
    plt.legend(loc='upper left')
    plt.subplot(4, 1, 4)
    plt.plot(residual, label='残差')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

np.random.seed(42)
seasonal_data = np.sin(np.linspace(0, 4 * np.pi, 100)) + np.random.normal(0, 0.5, 100)
time_index = pd.date_range(start='2023-01-01', periods=100, freq='M')
time_series = pd.Series(seasonal_data, index=time_index)

seasonal_decompose_plot(time_series, model='additive')