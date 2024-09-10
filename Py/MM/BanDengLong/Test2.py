import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

k = 0.55 / (2 * np.pi)


def soLve_theta(t):
    x = sp.symbols('x')

    # 定义一元二次方程 ax^2 + bx + c = 0

    # 构造方程

    equation = sp.Eq(x ** 2 * (1 + x * x) * k ** 2, (884-t) ** 2)

    # 求解方程
    solutions = sp.solve(equation, x)
    theta = solutions[1]
    return theta


def calculate_xy(theta):
    x = k*theta * np.cos(float(theta))
    y = k*theta * np.sin(float(theta))
    return x, y

# def find_next_theta(theta1, d, iterations=223):
#     theta_next = theta1
#     for _ in range(iterations):
#         print(theta1)
#         found = False
#         for theta2 in np.linspace(theta_next + 0.01, theta_next + 2 * np.pi, 10000):
#             x1, y1 = calculate_xy(theta_next)
#             x2, y2 = calculate_xy(theta2)
#             distance = np.sqrt(float((x2 - x1)**2 + (y2 - y1)**2))
#
#             if np.isclose(distance, d, atol=0.01):
#                 theta_next = theta2
#                 found = True
#                 break  # Break the inner loop if a close enough point is found
#
#         if not found:
#             break  # Break the outer loop if no point is found in the current iteration
#
#     return theta_next

# 主程序
t = 100
d_first = 2.86  # 第一个红点与黑点之间的距离
d_next = 1.65  # 后续点之间的距离

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

theta_black = soLve_theta(300)
r_black = k * theta_black
ax.plot(theta_black, r_black, 'ko')  # 画黑点

# # 找到第一个红点
# theta_red = find_next_theta(theta_black, d_first, 1)
# if theta_red is not None:
#     r_red = 0.55 / (2 * np.pi) * theta_red
#     # ax.plot(theta_red, r_red, 'ro')  # 画第一个红点
#     # ax.plot([theta_black, theta_red], [r_black, r_red], 'b-')  # 连接黑点和第一个红点
#
# # 基于第一个红点找到后续的点并绘制
# theta_next = theta_red
# for _ in range(223):
#     theta_next = find_next_theta(theta_next, d_next, 1)
#     if theta_next is None:
#         break
#     r_next = 0.55 / (2 * np.pi) * theta_next
#     # ax.plot(theta_next, r_next, 'ro')  # 画后续的红点

plt.show()
