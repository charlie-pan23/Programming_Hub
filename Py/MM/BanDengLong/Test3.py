import numpy as np
import matplotlib.pyplot as plt

def calculate_theta(t):
    target = 2 * np.pi / 0.55 * (884 - t)
    theta_guess = 1.0
    for _ in range(100):
        theta_guess -= (theta_guess * np.sqrt(1 + theta_guess**2) - target) / (np.sqrt(1 + theta_guess**2) + theta_guess**2 / np.sqrt(1 + theta_guess**2))
    return theta_guess

def calculate_xy(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def find_closest_theta2(theta1, r1, d):
    min_diff = np.inf
    theta2_best = None
    for theta2 in np.linspace(theta1 + 0.01, theta1 + 2 * np.pi, 10000):
        r2 = 0.55 / (2 * np.pi) * theta2
        x1, y1 = calculate_xy(r1, theta1)
        x2, y2 = calculate_xy(r2, theta2)
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if np.isclose(distance, d, atol=0.01):
            diff = theta2 - theta1
            if diff < min_diff:
                min_diff = diff
                theta2_best = theta2
    return theta2_best

# 设定特定的t值
t = 100
d = 2  # 设定一个d值

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')

theta1 = calculate_theta(t)
r1 = 0.55 / (2 * np.pi) * theta1
ax.plot(theta1, r1, 'ko')  # 画黑点

theta2 = find_closest_theta2(theta1, r1, d)
if theta2 is not None:
    r2 = 0.55 / (2 * np.pi) * theta2
    ax.plot(theta2, r2, 'ro')  # 画红点
    # 连接红点和黑点的蓝色线
    ax.plot([theta1, theta2], [r1, r2], 'b-')

plt.show()
