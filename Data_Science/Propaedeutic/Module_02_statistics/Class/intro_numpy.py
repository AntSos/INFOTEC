#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:29:15 2026

@author: irukandji
"""

import numpy as np

# Firs array, dtype int64
arr_1 = np.array([1, 2, 3 ,4, 5])

print(arr_1, type(arr_1))
# Normal list, normal python value.
normal_list = [1, 2, 3 ,4, 5]

# Matrix array.
arr_2 = np.array([
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ])

print(arr_2)
# Slice and assign a new value to a specific element.
arr_2[1][2] = 111
print(arr_2)
# Reshape the array.
arr_2.shape = (1, 9)
print(arr_2)

"""Data type"""
print()
# Array 8 bits -128 a 127.
arr_int8 = np.array([_ for _ in range(11, 100, 11)], dtype='int8')
print(arr_int8)


"""Automatic arrays"""
print()
zeros = np.zeros(3)
print(zeros)
zeros_2 = np.zeros((2,2))
print(zeros_2)
ones = np.ones((4, 5))
print(ones)
identity = np.identity(6)
print(identity)
eye_matrix = np.eye(3, 4)
print(eye_matrix)

arr_3 = np.array([
                    [1, 2, 3],
                    [4, 5, 6]
                    ], dtype=np.int32)

print(arr_3)
# Same dimension as the passed array.
ones_2 = np.ones_like(arr_3)
print(ones_2)
# From 11 to 100, incresing 11 each element.
steps_1 = np.arange(11, 100, 11)
print(steps_1)
# Reshape to a 3X3.
steps_2 = np.arange(11, 100, 11).reshape((3, 3))
print(steps_2)
# Uniform model, five elemnt from 0 to 1, with uniform space value between them.
line_1 = np.linspace(0, 1, 5)
print(line_1)
# Random values.
random_values = np.random.random(100)
print(random_values)

"""Attributes and properties"""
print()
arr_4 = np.array([
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ])


print(f"Shape {arr_4.shape}")
print(f"Dimenssion {arr_4.ndim}")
print("Type {arr_3.dtype}")
print(f"Size {arr_4.size}")

"""Mathematic opperatons"""

arr_5 = np.array([10, 20, 30])
arr_6 = np.array([1, 2 ,3])

print(f"Sum {arr_5 + arr_6}")
print(f"Multiplication  {arr_5 * arr_6}")
print(f"Pow  {arr_5 **2}")
print(f"Sin  {np.sin(np.radians(arr_5))}")


"""Indexing and slicing"""
print()
matrix_2 = np.array([[10, 20, 30], 
                     [40, 50, 60], 
                     [70, 80, 90]
                     ])

print(matrix_2[1, 2], end="\n\n")
print(matrix_2[0, :], end="\n\n")
print(matrix_2[:, 1], end="\n\n")
print(matrix_2[:2, :2], end="\n\n")




"""Reshaping"""

original = np.arange(12)

new_reshape = original.reshape(3, 4)

transponse = new_reshape.T

print(new_reshape)
print(transponse)


"""Basic Statistics"""
print()

data = np.array([[1, 2], [3, 4]])
# Sum.
print(f"Summ: {np.sum(data)}")
print(f"Averange: {np.mean(data)}")
print(f"Standar deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Sum columns: {np.sum(data, axis=0)}")
print(f"Sum rows: {np.sum(data, axis=1)}")
print(f"Minimun: {np.min(data)}")
print(f"Maximun {np.max(data)}")

""" Boolean Masks"""

numbers = np.array([1, 15, 8, 20, 3, 12])
# Conditional filter.
greater_10 = numbers[numbers >= 10]
# Boolean result.
result = numbers >= 10
print(greater_10)
print(result)
numbers.sort()
print(numbers)



"""More functions"""
arr_7 = np.array([11, 22, 33, 44])
arr_8 = np.array([55, 66, 77, 88])

print(np.concatenate((arr_7, arr_8)))


arr_9 = np.array([[1, 1], [2, 2]])
arr_10 = np.array([[3, 3], [4, 4]])
# Vertical stack.
print(np.vstack((arr_9, arr_10)))
# Horizontal stack.
print(np.hstack((arr_9, arr_10)))
# Unique elements.
arr_11 = np.array([11, 11, 22, 22, 11, 33, 44, 99, 11, 33, 66])
print(np.unique(arr_11))
