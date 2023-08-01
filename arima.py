import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# 示例数据
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# 将数据转换为时间序列对象
index = pd.date_range(start='2023-01-01', periods=len(data), freq='MS')
ts_data = pd.Series(data, index=index)

# 假设我们已经知道ARIMA模型的阶数为(p, d, q) = (1, 1, 1)
p, d, q = 1, 2, 1

# 创建ARIMA模型
model = ARIMA(ts_data, order=(p, d, q))

# 拟合ARIMA模型
results = model.fit()

# 获取AIC和BIC值
aic = results.aic
bic = results.bic

# 输出AIC和BIC值
print("AIC值: ", aic)
print("BIC值: ", bic)
