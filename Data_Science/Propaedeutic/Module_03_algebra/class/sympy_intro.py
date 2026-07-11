#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:43:34 2026

@author: irukandji
"""

import sympy as sp

x, y, z, a, b, c = sp.symbols('x y z a b c')

eq1 = sp.Eq(x + y, a)
eq2 = sp.Eq(x - y, b)
eq3 = sp.Eq(y, c)

sol = sp.solve((eq1, eq2, eq3), (x, y, a, b, c))

print(sol, end='\n\n')

eq4 = sp.Eq(-5*x -4*y + 10*z, a)
eq5 = sp.Eq(-8*x -8*y - 5*z, b)

print(sp.solve((eq4, eq5), (x, y, z, a, b)), end='\n\n')

# Determinant
A = sp.Matrix([[1, -2], [-3, 7]])

print(A.det(), end='\n\n')

B = sp.Matrix([[2, 0], [1, -1]])
print(B.det(), end='\n\n')

C = sp.Matrix([[1, 5, 2], [2, 0, 1], [1, -1, 1]])
print(C.det(), end='\n\n')

D = sp.Matrix([[5, -2, 4], [0, 1, 5], [1, 2, -8]])
print(D.det(), end='\n\n')


E = sp.Matrix([[1, 2], [3, 4]])

print(E.charpoly('l'))

F = sp.Matrix([[3, 2], [2, 0]])

print(F.eigenvals(F), end='\n\n')
print(F.eigenvects(F), end='\n\n')