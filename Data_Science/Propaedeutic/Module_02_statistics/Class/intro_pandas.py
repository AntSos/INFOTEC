#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:35:11 2026

@author: irukandji
"""

import pandas as pd
import numpy as np

ages = pd.Series([25, 30, 35, 40], name='Age')
names = pd.Series(['Antonio', 'Mike', 'Gabriela'])

table = pd.concat([names, ages], axis = 1)

data = {
        'Motor': ['AC_standart', 'Servo', 'Stepper'],
        'Voltage': [220, 24, 12],
        'Efficiencie': [True, True, True]
        }

df = pd.DataFrame(data)
print(df)

df_auto = pd.read_csv('automobile_parts.csv')
print(df_auto)