# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:33:06 2020

@author: Ajie
"""

import matplotlib.pyplot as plt

def f(x):
    return x ** 4

def df(x):
    return 4*x ** 3

def df2(x):
    return 12*x**2



cur_x = 1
xs = [i for i in range(101)]
ys = [1]
ys2 = [1]
ys3 = [1]
ys4 = [1]
ys5 = [1]
ys6 = [1]

for i in range(100):
    cur_x = cur_x - 0.1 * df(cur_x)
    ys.append(f(cur_x))

cur_x = 1
for i in range(100):
    cur_x = cur_x - 0.01 * df(cur_x)
    ys2.append(f(cur_x))

cur_x = 1
for i in range(100):
    if cur_x != 0:
        cur_x = cur_x - 0.25 *(cur_x ** (-2)) * df(cur_x)
    ys3.append(f(cur_x))


cur_x = 1
for i in range(100):
    cur_x = cur_x - 1 * df(cur_x) / df2(cur_x)
    ys4.append(f(cur_x))

cur_x = 1
for i in range(100):
    cur_x = cur_x - 0.1 * df(cur_x) / df2(cur_x)
    ys5.append(f(cur_x))


cur_x = 1
for i in range(100):
    cur_x = cur_x - 0.01 * df(cur_x) / df2(cur_x)
    ys6.append(f(cur_x))



plt.plot(xs,ys,label='0.1')
plt.plot(xs,ys2,label='0.01')
plt.plot(xs,ys3,label='optimal')
plt.plot(xs,ys4,label='newton_1')
plt.plot(xs,ys5,label='newton_0.1')
plt.plot(xs,ys6,label='newton_0.01')

plt.xlabel('Iteration')
plt.ylabel('Value ')
plt.legend()
plt.show()

    