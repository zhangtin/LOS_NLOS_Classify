import numpy as np
from scipy.constants import c
from scipy.io import loadmat
import LOS_Classify as LC
# 参数设置初始化
fc = 5520e6  # 信号载波频率
lambda_ = c / fc  # 波长计算
q = 2 * np.pi / lambda_
d = lambda_ / 2  # 元件间距设置
N = 4  # 天线数量

# 波束形成设置
azi = np.arange(-90, 91, 1)  # 方位角
ucor = np.sin(np.deg2rad(azi))
ucor_matrix = np.exp(-1j * q * d * np.arange(N)[:, None] * ucor)  # 波束成形权重

# 可选参数
Scan_interval = 10  # 加速用

# 加载波形
sig = loadmat("D:/Research_Files/LOS_NLOS/Datas/QPSK_new/LOS/1.mat")['data']  # 加载信号

# 信号分离
I = sig @ ucor_matrix

# 检查是否为LOS
Result = LC.LOS_Classify(I, Scan_interval)

# 显示结果
if Result == 1:
    print("Signal from LOS")
else:
    print("Signal from NLOS")
