# import random
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import numpy as np
# import matplotlib.pyplot as plt
#
# def find_1(k):
#     # 生成1到1000的随机数列
#     numbers = list(range(1, 1001))
#     random.shuffle(numbers)
#     # 检查k的有效性
#     # if k <= 0 or k >= 1000:
#     #     # print("k should be between 0 and 1000")
#     #     return
#
#     # 查看并记录前k个
#     observed = numbers[:k]
#     # print(f"The front {k} secretaries observed are: {observed}")
#
#     # 与前k个对比，寻找"更好"的那个
#     for number in numbers[k:]:
#         if number > max(observed):
#             # print(f"The one been chosen is: {number}")
#             return number
#     # print(f"no one is chosen, so keep the last one:{numbers[1000]}")
#     return numbers[-1]
#
#
# # # 从用户输入获取k值
# # k = int(input("请输入k的值: "))
# results = np.zeros((2, 200))
#
# # 循环1000次，对1-1000的每个数字
# for i in range(1, 201):
#     # 记录每次调用find_1的结果，共计10次
#     sum_res = 0
#     for j in range(500):
#         sum_res += find_1(i)
#     # 计算平均值
#     avrg_res = sum_res / 500
#
#     # 将输入及其对应的输出平均值存入数组
#     results[0, i - 1] = i
#     results[1, i - 1] = avrg_res
#     print(i)
#
# # 使用Matplotlib绘制线性图
# plt.figure(figsize=(10, 6))
# plt.plot(results[0], results[1], label='Result')
# plt.title('Input vs. Average Output')
# plt.xlabel('Input Value')
# plt.ylabel('Average Output Value')
# plt.legend()
# plt.grid(True)
# plt.show()

####################################################

# import numpy as np
# import matplotlib.pyplot as plt
#
# n = 1000
#
# def cal_k(k):
#     sum_k = 0.0
#     for i in range(k,n):  # 从k遍历到n
#         sum_k += 1/i
#     ans = k/n * sum_k
#     return ans
#
# results = np.zeros((2, n))
#
# # 使用循环填充结果
# for i in range(1, n+1):
#     results[0, i-1] = i  # 储存k值
#     results[1, i-1] = cal_k(i)  # 储存计算得到的值
#     print(i)
#
# # 绘图
# plt.figure(figsize=(10, 6))
# plt.plot(results[0], results[1], label='P')
# plt.title('P with different k')
# plt.xlabel('k')
# plt.ylabel('P')
#
# # 寻找并标注最高点
# max_index = np.argmax(results[1])  # 找到P值最大的索引
# max_k = results[0, max_index]  # 对应的k值
# max_P = results[1, max_index]  # 最大的P值
#
# # 在图上标注最高点
# plt.scatter(max_k, max_P, color='red')
# plt.text(max_k, max_P, f'({max_k}, {round(max_P, 2)})', ha='right', va='bottom')
#
# plt.legend()
# plt.grid(True)
# plt.show()

#######################################################

import numpy as np
import matplotlib.pyplot as plt

n = 1000

def cal_k(k):
    sum_k = 0.0
    for i in range(k,n):  # 从k遍历到n
        sum_k += 1/i
    ans = k/n * sum_k
    return ans

results = np.zeros((2, n))

# 使用循环填充结果
for i in range(1, n+1):
    results[0, i-1] = i  # 储存k值
    results[1, i-1] = cal_k(i)  # 储存计算得到的值
    print(i)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(results[0], results[1], label='P')
plt.title('P with different k')
plt.xlabel('k')
plt.ylabel('P')

# # 寻找并标注最高点
# max_index = np.argmax(results[1])  # 找到P值最大的索引
# max_k = results[0, max_index]  # 对应的k值
# max_P = results[1, max_index]  # 最大的P值
#
# # 在图上标注最高点
# plt.scatter(max_k, max_P, color='red')
# plt.text(max_k, max_P, f'({max_k}, {round(max_P, 2)})', ha='right', va='bottom')

plt.legend()
plt.grid(True)
plt.show()
