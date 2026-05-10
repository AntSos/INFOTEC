#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:16:24 2026

@author: irukandji
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3]
y = [4, 5, 6]
plt.plot(x, y)
plt.show()
plt.bar(x, y, width= 0.3)
plt.show()

x1 = np.array([5, 7, 8, 7, 2, 9, 4, 11, 12, 9, 6])
y2 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77])

plt.scatter(x1, y2)
plt.xticks(np.arange(2, 19, 1))
plt.yticks(np.arange(min(y), max(y), 10))

plt.title('Graph_01')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.savefig('Graph_01.png', dpi=300, bbox_inches='tight')
plt.show()

fruits = ['apple', 'mangos', 'strawberries']
sell = [10, 15, 7]

plt.bar(fruits, sell)
plt.show()

x3 = np.array([_ for _ in range(30)])
y3 = np.array([np.random.randint(0, 100) for _ in range(30)])

plt.plot(x3, y3)
plt.show()

x4 = np.linspace(0, 2 , 100)
f1 = np.copy(x4)
f2 = np.copy(x4)**2
f3 = np.copy(x4)**3
print(hex(id(x4)), hex(id(f1)))

# Multiple graphs.
plt.figure(figsize=(5, 3))
plt.subplot(131)
plt.plot(x4, f1)
plt.title('Fun 1')
plt.subplot(132)
plt.plot(x4, f2)
plt.title('Fun 2')
plt.subplot(133)
plt.plot(x4, f3)
plt.title('Fun 3')
plt.show()

# Full graph.

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x4, f1, label='Fun 1')
ax.plot(x4, f2, label='Fun 2')
ax.plot(x4, f3, label='Fun 3')
ax.set_xlabel('f(x)')
ax.set_ylabel('Response')
ax.legend()

n_f = np.sin(np.linspace(0, 10, 100))

x5 = np.arange(len(n_f))

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x5, n_f, color = 'purple', linewidth=1, linestyle='--')