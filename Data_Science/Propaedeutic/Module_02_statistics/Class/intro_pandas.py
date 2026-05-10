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
print(table)

data = {
        'Motor': ['AC_standart', 'Servo', 'Stepper'],
        'Voltage': [220, 24, 12],
        'Efficiencie': [True, True, True]
        }

df = pd.DataFrame(data)
print(df)
print()
""" 
Doc mannagement
    - .csv
    - .xls, .xlsx
    - .json
    - .SQL
"""
df_auto = pd.read_csv('automobile_parts.csv')
print(df_auto, end='\n\n')
print(df_auto.head(15), end='\n\n')
print(df_auto.tail(15), end='\n\n')
print(df_auto.info(), end='\n\n')
description = df_auto.describe()
print(description, end='\n\n')

"""Indexing and slicing"""
keys_df_auto = df_auto.keys()
print(keys_df_auto, end='\n\n')
print(list(keys_df_auto))

for i, j in zip(df_auto.columns, list(df_auto.columns)):
    print(f"{i}, - {j}", end = " , ")
    
print()

# Specific column
print(df_auto['TYPE'], end='\n\n')
# Specific column and row.
print(df_auto['TYPE'][121], end='\n\n')
# Specific row using .loc[]
print(df_auto.loc[121], end='\n\n')
# Specific rows and columns.
print(df_auto.iloc[0:2, 0:3], end='\n\n')
# Only items > 400
expensive_items = df_auto[df_auto['PRICE'] > 400]
print(expensive_items, end='\n\n')
# Only items from audi and > 450.
only_audi = df_auto[(df_auto['MANUFACTURER'] == 'Audi') & (df_auto['PRICE'] > 450)]
print(only_audi, end='\n\n')

""" Cleaning and modifing data"""
# Add a new column.
df_auto['QUANTITY'] = 0
print(df_auto, end='\n\n')
# Add random number to quantity column, it will create the column if it does not exist.
df_auto['QUANTITY'] = [np.random.randint(1, 100) for _ in range(len(df_auto))]
print(df_auto, end='\n\n')
# Change colum posistion.
df_auto = df_auto[['PART ID', 'TYPE', 'MANUFACTURER', 'YEAR', 'QUANTITY', 'PRICE']]
print(df_auto, end='\n\n')
# Add another column and assign an opperation value.
df_auto['SUBTOTAL_INVENTORY'] = df_auto['QUANTITY'] * df_auto['PRICE']
print(df_auto, end='\n\n')
# Rename a column.
df_auto = df_auto.rename(columns={'PART ID': 'PART_ID'})
print(df_auto, end='\n\n')
# Add another column
df_auto['ACTIVE'] = [np.random.choice([True, False, np.nan]) for _ in range(len(df_auto))]
print(df_auto, end='\n\n')
# Add a new row element at the end of the df.
df_auto.loc[len(df_auto)] = ['PARTXXX', 'Spring', 'Nissan', 2026, np.nan, 100.11, np.nan, 1]
# Print the last item.
print(df_auto.iloc[[-1]], end='\n\n')

""" Export results """

df_auto.to_csv('Inventory_20260509.csv')