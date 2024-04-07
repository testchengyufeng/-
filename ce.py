
import numpy as np
import matplotlib.pyplot as plt
# 创建时间向量t，从1到15，间隔为0.2
t = np.arange(1, 15.1, 0.2)
# 计算信号A
A = np.sin(2 * np.pi * t) + np.cos(2 * np.pi * 0.5 * t)
# 添加噪声到信号A中
Anoise = A + 0.5 * np.random.rand(len(t))
# 绘制原始数据和带噪声的数据
plt.plot(t, A, label="Original Data")
plt.plot(t, Anoise, label="Noisy Data")
# 调整坐标轴范围以紧密贴合数据
plt.axis('tight')
# 添加图例
plt.legend()
# 显示图形
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.io as sio
# 加载.mat文件
data = sio.loadmat('windData.mat')
speed = data['speed']  # 假设speed是.mat文件中的变量名
# 创建时间索引数组
mins = np.arange(1, len(speed) + 1)
# 计算移动平均的窗口大小
window = 5
# 使用numpy的convolve函数和ones数组来计算移动平均
ones = np.ones(window) / window
meanspeed = np.convolve(speed, ones, mode='same')
# 绘图
plt.figure(figsize=(10, 6))
plt.plot(mins, speed, label="Measured Wind Speed", color='blue')
plt.plot(mins, meanspeed, label="Average Wind Speed over 5 min Window", color='red', linestyle='--')
# 设置图表样式
plt.axis('tight')  # 等比例缩放图表
plt.legend()  # 显示图例
plt.xlabel("Time")  # x轴标签
plt.ylabel("Speed")  # y轴标签
plt.title('Wind Speed over Time with 5-min Moving Average')  # 添加标题
# 显示图表
plt.show()
