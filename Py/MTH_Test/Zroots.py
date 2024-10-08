import numpy as np
import matplotlib.pyplot as plt

# 定义复数的实部和虚部
z0 = np.exp(1j * np.pi/12) * np.power(2, 1/6)
z1 = np.exp(1j * 3*np.pi/4) * np.power(2, 1/6)
z2 = np.exp(1j * 17*np.pi/12) * np.power(2, 1/6)

# 绘制复平面
plt.figure(figsize=(10,10))
plt.plot([0, z0.real], [0, z0.imag], 'ro')  # z0
plt.plot([0, z1.real], [0, z1.imag], 'bo')  # z1
plt.plot([0, z2.real], [0, z2.imag], 'go')  # z2
plt.plot([z0.real, z1.real], [z0.imag, z1.imag], 'k--')  # 连接线
plt.plot([z1.real, z2.real], [z1.imag, z2.imag], 'k--')  # 连接线
plt.plot([z2.real, z0.real], [z2.imag, z0.imag], 'k--')  # 连接线

# 绘制虚线圆
circle = plt.Circle((0, 0), np.power(2, 1/6), color='gray', fill=False, linestyle='--', linewidth=1)
plt.gca().add_artist(circle)

# 设置复平面的标签和标题
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Roots')
plt.grid(True)
plt.axis('equal')  # 确保x和y轴的刻度相同

# 设置坐标轴的范围
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# 显示图形
plt.show()