import pdb
import pdb
import sympy as sp
import numpy as np
from sympy.codegen import Print


# 定义变量

def soLve_theta(t):
    x = sp.symbols('x')c

    # 定义一元二次方程 ax^2 + bx + c = 0

    # 构造方程
    k = 0.55/(2*np.pi)

    equation = sp.Eq(x ** 2 * (1 + x * x) * k ** 2, (884-t) ** 2)

    # 求解方程
    solutions = sp.solve(equation, x)
    theta = solutions[1]
    return theta

print(soLve_theta(100))
#
k = 0.55 / (2 * sp.pi)


def soLve_theta(theta):
    x = sp.symbols('x')
    theta = sp.rad(theta)


    # 构造方程
    c1 = k*theta*sp.cos(theta)
    c2 = k*theta*sp.sin(theta)
    pdb.set_trace()
    equation = sp.Eq(k*k*x*x-2*k*c1*x*sp.cos(x)-2*k*c2*x*sp.sin(x)+c1*c1+c2*c2,2.86*2.86)
    print(1)
    # 求解方程
    solutions = sp.solve(equation, x)
    print(2)
    return solutions


print(soLve_theta(90))