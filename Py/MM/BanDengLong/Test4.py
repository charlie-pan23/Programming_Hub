import matplotlib.pyplot as plt
import numpy as np
import time

# 参数定义
L_head = 2.86
L_body = 1.65
pitch = 0.55
v_head = 1
theta0 = 16 * 2 * np.pi
t_total = 300
dt = 1
num_sections = 223

# 计算龙头的初始半径和角速度
initial_radius_head = pitch * theta0 / (2 * np.pi)
angular_velocity = v_head / initial_radius_head

# 初始化矩阵
time_steps = t_total + 1
positions = np.zeros((time_steps, num_sections, 2))

# 计算每节板凳的每秒位置
for t in range(t_total + 1):
    # 计算龙头位置
    theta = theta0 - angular_velocity * t
    r_head = pitch * theta / (2 * np.pi)
    positions[t, 0] = [r_head * np.cos(theta), r_head * np.sin(theta)]

    # 计算每节板凳的位置
    current_theta = theta
    current_radius = r_head
    for i in range(1, num_sections):
        arc_length = L_head if i == 1 else L_body
        delta_theta = arc_length / current_radius
        current_theta += delta_theta
        current_radius = pitch * current_theta / (2 * np.pi)
        positions[t, i] = [current_radius * np.cos(current_theta), current_radius * np.sin(current_theta)]

# 绘制螺旋线作为背景
theta_values = np.linspace(0, theta0, 1000)
r_values = pitch * theta_values / (2 * np.pi)
x_spiral = r_values * np.cos(theta_values)
y_spiral = r_values * np.sin(theta_values)

# 绘制每个t时刻的舞龙队状态和螺旋线背景
plt.ion()
fig, ax = plt.subplots()
for t in range(t_total + 1):
    ax.clear()
    ax.plot(x_spiral, y_spiral, 'r-', linewidth=1.5)
    ax.plot(positions[t, :, 0], positions[t, :, 1], 'bo-', markersize=4)
    ax.set_title(f'舞龙队在第{t}秒的状态')
    ax.set_xlabel('X 位置 (m)')
    ax.set_ylabel('Y 位置 (m)')
    ax.axis('equal')
    ax.grid(True)
    plt.draw()
    plt.pause(0.5)
plt.ioff()
plt.show()
